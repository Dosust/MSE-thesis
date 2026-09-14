import importlib.util, pathlib, pandas as pd
p=pathlib.Path(__file__).with_name("row_level_audit_runner.py")
spec=importlib.util.spec_from_file_location("audit",p)
a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a)

def test_complete_frame():
    df=pd.DataFrame({
      "data_as_of":["2023-12-17T00:00:00","2023-12-17T00:05:00","2023-12-17T00:10:00"],
      "link_id":["1","1","1"],"speed":["20","21","22"],"travel_time":["60","58","55"],
      "status":["0","0","0"],"borough":["Bronx"]*3,"link_name":["x"]*3
    })
    m=a.audit_frame(df,"NYC_DOT_SPEEDS","2023-12-17T00:00:00","2023-12-17T00:10:00")
    assert m["n_rows"]==3
    assert abs(m["median_dt_s"]-300)<1e-9
    assert m["required_field_null_rate_max"]==0
    assert m["duplicate_rate"]==0
    assert m["R1"] and m["R2"] and m["R5"]

def test_duplicate_detection():
    df=pd.DataFrame({
      "unique_key":["1","1"],"created_date":["2020-08-04T00:00:00"]*2,
      "agency":["DOT"]*2,"complaint_type":["Tree"]*2,"descriptor":["Downed"]*2,
      "status":["Open"]*2,"borough":["Bronx"]*2,"latitude":[40.8]*2,"longitude":[-73.9]*2
    })
    m=a.audit_frame(df,"NYC_311","2020-08-04T00:00:00","2020-08-04T00:00:00")
    assert abs(m["duplicate_rate"]-0.5)<1e-12

def test_eaglei_missingness_gate():
    df=pd.DataFrame({
      "fips_code":["36005"],"county":["Bronx"],"state":["New York"],"sum":[100],
      "run_start_time":["2020-08-04T12:00:00Z"]
    })
    m=a.audit_frame(df,"EAGLEI","2020-08-04T00:00:00","2020-08-05T00:00:00")
    assert m["R3"] is False

def test_required_field_failure():
    df=pd.DataFrame({"data_as_of":["2023-12-17T00:00:00"]})
    m=a.audit_frame(df,"NYC_DOT_SPEEDS","2023-12-17T00:00:00","2023-12-18T00:00:00")
    assert m["R5"] is False

if __name__=="__main__":
    test_complete_frame(); test_duplicate_detection(); test_eaglei_missingness_gate(); test_required_field_failure()
    print("4/4 offline audit tests passed")
