// ZOTERO — identify the earlier 10 selected engineering-sustainability papers
// and add them to a subcollection of the currently selected collection.
// This script does NOT delete or move items.

const SUBCOLLECTION_NAME = "Top 10 Engineering-Sustainability Papers";

const TARGETS = [
    {rank:1,csvID:"245",doi:"10.1016/j.engstruct.2019.03.021",title:"Linking seismic resilience into sustainability assessment of limited-ductility RC buildings"},
    {rank:2,csvID:"241",doi:"10.1016/j.jobe.2024.109368",title:"Low carbon concrete for prefabricated modular construction in circular economy: An integrated approach towards sustainability, durability, cost, and mechanical performances"},
    {rank:3,csvID:"232",doi:"10.1016/j.jclepro.2022.131900",title:"Experimental characterization of comfort performance parameters and multi-criteria sustainability assessment of recycled textile-reinforced cement facade cladding"},
    {rank:4,csvID:"59",doi:"10.1016/j.eiar.2025.108191",title:"Innovative safety framework and direct load–settlement method to optimize vertical subgrade modulus in sustainable mat foundations"},
    {rank:5,csvID:"124",doi:"10.1016/j.resconrec.2025.108335",title:"Integrated environmental, economic, and performance assessments of cold recycling technologies for asphalt pavements"},
    {rank:6,csvID:"169",doi:"10.1016/j.jclepro.2024.144108",title:"Sustainability assessment of granite cutting waste incorporated cement sand rendering mortar: Technical, environmental, cost, and social parameters"},
    {rank:7,csvID:"282",doi:"10.1016/j.jclepro.2022.133064",title:"Life cycle sustainable assessment of natural vs artificial lightweight aggregates"},
    {rank:8,csvID:"83",doi:"10.1016/j.jobe.2023.107406",title:"Serviceability parameters and social sustainability assessment of flax fabric reinforced lime-based drywall interior panels"},
    {rank:9,csvID:"23",doi:"10.1016/j.buildenv.2014.10.013",title:"An integrated energy-emergy approach to building form optimization: Use of EnergyPlus, emergy analysis and Taguchi-regression method"},
    {rank:10,csvID:"10",doi:"10.1016/j.engstruct.2019.109968",title:"Robust decision-making design for sustainable pedestrian concrete bridges"}
];

function normalizeDOI(value) {
    return String(value || "").trim().toLowerCase()
        .replace(/^https?:\/\/(dx\.)?doi\.org\//, "")
        .replace(/^doi:\s*/i, "");
}

function normalizeTitle(value) {
    return String(value || "").normalize("NFKC").toLowerCase()
        .replace(/[‐‑‒–—−]/g, "-")
        .replace(/[“”]/g, '"')
        .replace(/[‘’]/g, "'")
        .replace(/\s+/g, " ")
        .trim();
}

const zp = Zotero.getActiveZoteroPane();
const parentCollection = zp.getSelectedCollection();
if (!parentCollection) throw new Error("STOP: Select the PARENT COLLECTION before running this script.");
const libraryID = parentCollection.libraryID;

let children = Zotero.Collections.getByParent(parentCollection.id, false, false);
let targetCollection = children.find(c => c.name === SUBCOLLECTION_NAME);
let collectionCreated = false;

if (!targetCollection) {
    targetCollection = new Zotero.Collection();
    targetCollection.libraryID = libraryID;
    targetCollection.name = SUBCOLLECTION_NAME;
    targetCollection.parentID = parentCollection.id;
    await targetCollection.saveTx();
    collectionCreated = true;
}

async function searchTarget(target) {
    let doiSearch = new Zotero.Search();
    doiSearch.libraryID = libraryID;
    doiSearch.addCondition("DOI", "is", target.doi);
    let doiIDs = await doiSearch.search();
    let doiItems = [];
    for (let id of doiIDs) {
        let item = await Zotero.Items.getAsync(id);
        if (item && item.isRegularItem() && !item.deleted && normalizeDOI(item.getField("DOI")) === normalizeDOI(target.doi)) doiItems.push(item);
    }
    if (doiItems.length === 1) return {status:"MATCHED_BY_DOI",item:doiItems[0]};
    if (doiItems.length > 1) return {status:"AMBIGUOUS_DUPLICATE_DOI",items:doiItems};

    let titleSearch = new Zotero.Search();
    titleSearch.libraryID = libraryID;
    titleSearch.addCondition("title", "is", target.title);
    let titleIDs = await titleSearch.search();
    let titleItems = [];
    for (let id of titleIDs) {
        let item = await Zotero.Items.getAsync(id);
        if (item && item.isRegularItem() && !item.deleted && normalizeTitle(item.getField("title")) === normalizeTitle(target.title)) titleItems.push(item);
    }
    if (titleItems.length === 1) return {status:"MATCHED_BY_TITLE",item:titleItems[0]};
    if (titleItems.length > 1) return {status:"AMBIGUOUS_DUPLICATE_TITLE",items:titleItems};
    return {status:"NOT_FOUND"};
}

let matchedItems = [];
let report = [];
for (const target of TARGETS) {
    const result = await searchTarget(target);
    if (result.status === "MATCHED_BY_DOI" || result.status === "MATCHED_BY_TITLE") {
        matchedItems.push(result.item);
        report.push({rank:target.rank,csvID:target.csvID,status:result.status,zoteroItemID:result.item.id,zoteroKey:result.item.key,doi:result.item.getField("DOI"),title:result.item.getField("title")});
    } else if (result.status === "AMBIGUOUS_DUPLICATE_DOI" || result.status === "AMBIGUOUS_DUPLICATE_TITLE") {
        report.push({rank:target.rank,csvID:target.csvID,status:result.status,matches:result.items.map(item => ({zoteroItemID:item.id,zoteroKey:item.key,doi:item.getField("DOI"),title:item.getField("title")}))});
    } else {
        report.push({rank:target.rank,csvID:target.csvID,status:"NOT_FOUND",expectedDOI:target.doi,expectedTitle:target.title});
    }
}

let uniqueItemIDs = [...new Set(matchedItems.map(item => item.id))];
if (uniqueItemIDs.length > 0) {
    await Zotero.DB.executeTransaction(async function () {
        await targetCollection.addItems(uniqueItemIDs);
    });
}

let finalChildIDs = targetCollection.getChildItems(true);
let verifiedInCollection = uniqueItemIDs.filter(id => finalChildIDs.includes(id));
let notFound = report.filter(r => r.status === "NOT_FOUND");
let ambiguous = report.filter(r => r.status.startsWith("AMBIGUOUS"));

return JSON.stringify({
    operation:"Top-10 paper collection assignment",
    parentCollection:parentCollection.name,
    subcollection:targetCollection.name,
    subcollectionCreated:collectionCreated,
    targetPapers:TARGETS.length,
    uniquelyMatched:uniqueItemIDs.length,
    verifiedAddedToCollection:verifiedInCollection.length,
    notFoundCount:notFound.length,
    ambiguousCount:ambiguous.length,
    success:uniqueItemIDs.length === 10 && verifiedInCollection.length === 10 && notFound.length === 0 && ambiguous.length === 0,
    records:report
}, null, 2);