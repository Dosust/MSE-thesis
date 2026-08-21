(* ::Package:: *)

(* Wolfram-Physics-Project-inspired editable scientific poster template
   Purpose: generate editable vector diagrams for sustainable/resilient infrastructure frameworks.
   Core computational graphics use Wolfram Language + Wolfram Function Repository.
   Final export: SVG/PDF for editing in Wolfram Desktop, Figma, Illustrator, Inkscape, etc.

   IMPORTANT:
   WolframPhysicsProjectStyleData currently documents only the Light project theme.
   This file therefore uses the official project style resource where appropriate,
   then defines a separate editable dark-poster theme inspired by the visual-summary poster.
*)

ClearAll["Global`*"];
Needs["GraphUtilities`"];

$PosterTheme = <|
  "Background" -> RGBColor[0.07, 0.075, 0.08],
  "PanelBackground" -> RGBColor[0.085, 0.09, 0.10],
  "Text" -> RGBColor[0.94, 0.95, 0.96],
  "MutedText" -> RGBColor[0.58, 0.61, 0.64],
  "Cyan" -> RGBColor[0.08, 0.62, 0.86],
  "Blue" -> RGBColor[0.10, 0.45, 0.75],
  "Orange" -> RGBColor[0.95, 0.55, 0.05],
  "Red" -> RGBColor[0.85, 0.16, 0.16],
  "Magenta" -> RGBColor[0.74, 0.18, 0.55],
  "Green" -> RGBColor[0.31, 0.72, 0.35],
  "Frame" -> RGBColor[0.22, 0.25, 0.28],
  "Guide" -> RGBColor[0.38, 0.40, 0.42]
|>;

SetOptions[{Graphics, Graph}, Background -> None];

titleStyle[s_] := Style[s, 28, Bold, FontFamily -> "Helvetica", $PosterTheme["Text"]];
subtitleStyle[s_] := Style[s, 16, FontFamily -> "Helvetica", $PosterTheme["Text"]];
sectionStyle[s_, c_:Automatic] := Style[s, 12, Bold, FontFamily -> "Helvetica", If[c === Automatic, $PosterTheme["Text"], c]];
smallStyle[s_] := Style[s, 9.5, FontFamily -> "Helvetica", $PosterTheme["MutedText"]];
formulaStyle[s_] := Style[s, 11, FontFamily -> "Times", $PosterTheme["Text"]];

panel[content_, title_:None, color_:Automatic, size_:Automatic] := Module[
  {fc = If[color === Automatic, $PosterTheme["Frame"], color], body},
  body = If[title === None, content, Column[{sectionStyle[title, fc], Spacer[5], content}, Spacings -> .5]];
  Framed[Pane[body, ImageSize -> size], Background -> $PosterTheme["PanelBackground"], FrameStyle -> Directive[fc, AbsoluteThickness[1]], RoundingRadius -> 2, FrameMargins -> 10]
];

callout[text_, color_:Automatic] := Framed[
  smallStyle[text],
  FrameStyle -> Directive[If[color === Automatic, $PosterTheme["Guide"], color], Dashed, AbsoluteThickness[.8]],
  Background -> None,
  FrameMargins -> 5
];

WPPStyleData[type_] := ResourceFunction["WolframPhysicsProjectStyleData"][type];
WPPStyledGraph[g_Graph, type_:"SpatialGraph"] := Module[{f}, f = ResourceFunction["WolframPhysicsProjectStyleData"][type, "Function"]; f[g]];

spatialGraph[g_Graph, imageSize_:330] := Graph[g, GraphLayout -> "SpringElectricalEmbedding", VertexStyle -> Directive[$PosterTheme["Cyan"], EdgeForm[None]], EdgeStyle -> Directive[$PosterTheme["Cyan"], Opacity[.55], AbsoluteThickness[.8]], VertexSize -> .06, ImageSize -> imageSize, Background -> None];

causalGraph[g_Graph, imageSize_:450] := LayeredGraphPlot[g, VertexStyle -> Directive[$PosterTheme["Orange"], EdgeForm[None]], EdgeStyle -> Directive[$PosterTheme["Orange"], Opacity[.55], AbsoluteThickness[.9]], ImageSize -> imageSize, Background -> None];

multiwayGraph[g_Graph, imageSize_:450] := LayeredGraphPlot[g, VertexStyle -> Directive[$PosterTheme["Blue"], EdgeForm[None]], EdgeStyle -> Directive[$PosterTheme["Blue"], Opacity[.45], AbsoluteThickness[.8]], ImageSize -> imageSize, Background -> None];

branchialGraph[g_Graph, imageSize_:400] := Graph[g, GraphLayout -> "SpringElectricalEmbedding", VertexStyle -> Directive[$PosterTheme["Magenta"], EdgeForm[None]], EdgeStyle -> Directive[$PosterTheme["Magenta"], Opacity[.7], AbsoluteThickness[1.0]], VertexSize -> .07, ImageSize -> imageSize, Background -> None];

blackHoleRule = {{0, 1}, {0, 2}, {0, 3}} -> {{1, 2}, {3, 2}, {3, 4}, {4, 3}, {4, 4}};
blackHoleInitial = {{0, 0}, {0, 0}, {0, 0}};
blackHoleCausal = ResourceFunction["WolframModel"][blackHoleRule, blackHoleInitial, 20, "CausalGraph"];
blackHolePlot = causalGraph[blackHoleCausal, 460];

mw = ResourceFunction["MultiwaySystem"][{"A" -> "BBB", "BB" -> "A"}, {"A"}, 7, "EvolutionCausalGraph"];
mwPlot = multiwayGraph[mw, 460];

SeedRandom[574];
infraVertices = Join[Table["P"<>ToString[i], {i,1,8}], Table["W"<>ToString[i], {i,1,8}], Table["T"<>ToString[i], {i,1,8}], Table["S"<>ToString[i], {i,1,8}]];
infraEdges = UndirectedEdge @@@ RandomSample[Subsets[infraVertices,{2}], 70];
infraGraph = Graph[infraVertices, infraEdges];
sectorColor[v_] := Which[StringStartsQ[v,"P"], $PosterTheme["Cyan"], StringStartsQ[v,"W"], RGBColor[0.10,0.55,0.95], StringStartsQ[v,"T"], $PosterTheme["Orange"], True, $PosterTheme["Magenta"]];
infraPlot = Graph[infraGraph, GraphLayout -> "SpringElectricalEmbedding", VertexStyle -> (v_ :> sectorColor[v]), EdgeStyle -> Directive[$PosterTheme["Cyan"], Opacity[.28], AbsoluteThickness[.65]], VertexSize -> .05, VertexLabels -> None, ImageSize -> 430, Background -> None];

frameworkSteps = {
  {"01", "PHYSICAL LAWS", $PosterTheme["Cyan"]},
  {"02", "COUPLED SYSTEM", $PosterTheme["Cyan"]},
  {"03", "DYNAMIC INTERFACES", $PosterTheme["Orange"]},
  {"04", "OBSERVATION / INVERSE PROBLEM", $PosterTheme["Orange"]},
  {"05", "HAZARD + UNCERTAINTY", $PosterTheme["Magenta"]},
  {"06", "SERVICE-STATE MAPPING", $PosterTheme["Cyan"]},
  {"07", "SUSTAINABLE / EQUITABLE SET", $PosterTheme["Orange"]},
  {"08", "VIABILITY / REACHABILITY", $PosterTheme["Green"]},
  {"09", "RECOVERY / CONTROL", $PosterTheme["Green"]},
  {"10", "LIFECYCLE DECISION", $PosterTheme["Orange"]}
};

stepBox[{n_,label_,c_}] := Framed[Row[{Style[n, 10, Bold, c], Spacer[8], Style[label, 10, Bold, $PosterTheme["Text"]]}], FrameStyle -> Directive[c, AbsoluteThickness[.8]], Background -> $PosterTheme["PanelBackground"], FrameMargins -> {{8,8},{5,5}}, ImageSize -> 460];
stepColumn = Column[Riffle[stepBox /@ frameworkSteps, Style["↓", 14, $PosterTheme["Guide"]]], Alignment -> Center, Spacings -> .15];

foundations = Grid[Partition[{
  panel[smallStyle["PDEs / conservation laws"], None, $PosterTheme["Cyan"], 180],
  panel[smallStyle["Graph & network science"], None, $PosterTheme["Cyan"], 180],
  panel[smallStyle["Inverse problems"], None, $PosterTheme["Orange"], 180],
  panel[smallStyle["Bayesian UQ"], None, $PosterTheme["Orange"], 180],
  panel[smallStyle["Viability / HJ"], None, $PosterTheme["Green"], 180],
  panel[smallStyle["Optimization / OR"], None, $PosterTheme["Orange"], 180],
  panel[smallStyle["Control theory"], None, $PosterTheme["Green"], 180],
  panel[smallStyle["Scientific AI"], None, $PosterTheme["Magenta"], 180]
}, 4], Spacings -> {1,1}];

poster = Framed[
  Column[{
    Row[{Column[{titleStyle["MATHEMATICAL PHYSICS OF SUSTAINABLE INFRASTRUCTURE"], subtitleStyle["Editable Wolfram-style framework poster"], smallStyle["Foundation → identification → uncertainty → service → viability → decision"]}], Spacer[40], callout["All text, graphs, colors and formulas are editable in this source."]}, Alignment -> Top],
    Spacer[12],
    Grid[{{
      Column[{panel[Column[{sectionStyle["SEQUENCE OF UPDATING EVENTS", $PosterTheme["Cyan"]], infraPlot, smallStyle["State evolution • failure • repair • adaptation"]}], None, $PosterTheme["Cyan"], 460], Spacer[8], panel[Column[{sectionStyle["SPATIAL INFRASTRUCTURE HYPERGRAPH", $PosterTheme["Cyan"]], infraPlot, smallStyle["P = power • W = water • T = transport • S = solid waste"]}], None, $PosterTheme["Cyan"], 460]}],
      panel[Column[{sectionStyle["MASTER CAUSAL / DECISION CHAIN", $PosterTheme["Orange"]], stepColumn}], None, $PosterTheme["Orange"], 500],
      Column[{panel[Column[{sectionStyle["CAUSAL GRAPH", $PosterTheme["Orange"]], blackHolePlot}], None, $PosterTheme["Orange"], 480], Spacer[8], panel[Column[{sectionStyle["MULTIWAY / ALTERNATIVE PATHS", $PosterTheme["Blue"]], mwPlot}], None, $PosterTheme["Blue"], 480]}]
    }}, Spacings -> {1.3,1.3}],
    Spacer[10],
    panel[Column[{sectionStyle["MATHEMATICAL FOUNDATIONS", $PosterTheme["Text"]], foundations}], None, $PosterTheme["Frame"], 1480]
  }, Spacings -> .4],
  Background -> $PosterTheme["Background"], FrameStyle -> None, FrameMargins -> 20
];

Export["WolframInspiredInfrastructurePoster.svg", poster, "SVG"];
Export["WolframInspiredInfrastructurePoster.pdf", poster, "PDF"];
Export["WolframInspiredInfrastructurePoster.png", Rasterize[poster, RasterSize -> 4000], "PNG"];

(* Session note: this template was an early computational starting point. The later Figma fidelity review rejected the boxed/card-heavy composition as insufficiently close to the Wolfram reference. Future visual work should retain the computational graph-generation ideas while moving toward open-field, dense causal/multiway visual grammar. *)
