use polars::prelude::*;
use linfa::prelude::*;
use ndarray::{Array1,Array2};
use std::fs::File;
use std::path::Path;
use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]
struct DataSet {
    x: Array2<f32>,
    y: Array1<f32>,
}

fn main() {
    let path = Path::new("../").join("data.csv");
    println!("{}", path.display());
    let file = File::open(path).expect("File not found");
    let df = CsvReader::new(file).finish().unwrap();

    // println!("{:?}", df.head(Some(5)));

    let categorical_columns = ["Country"];
    let numerical_columns = ["Age", "Salary"];
    
    let x = df.select(["Country", "Age", "Salary"]);
    let y = df.select(["Purchased"]);
    

    

    // let data = DataSet {
    //     x: df.column("Country").expect("Column not found"),
    //     y: df.column("Purchased").expect("Column not found")
    // };

    // println!("{:?}", x);
    
}
