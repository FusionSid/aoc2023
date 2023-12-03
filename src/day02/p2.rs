use std::cmp;
use std::collections::HashMap;
use std::env;
use std::fs;
use std::path::PathBuf;
use std::process;

fn get_input_file_path(file_name: &str) -> PathBuf {
    if let Ok(exe_path) = env::current_exe() {
        if let Some(exe_dir) = exe_path.parent() {
            let input_path = exe_dir.join(file_name);
            return input_path;
        }
    }
    println!("Unable to get the path :(");
    process::exit(1);
}

fn get_input_data() -> String {
    let input_path = get_input_file_path("input.txt");
    return fs::read_to_string(input_path).expect("Should have been able to read the file");
}

fn main() {
    let binding = get_input_data();
    let data: Vec<_> = binding.split("\n").collect();

    let mut total = 0;
    for game in data.iter() {
        let game_data: Vec<_> = game.trim().split(": ").collect::<Vec<_>>();
        let subsets: Vec<_> = game_data[1].split("; ").collect();

        let (mut mr, mut mg, mut mb) = (0, 0, 0);

        for set in subsets.iter() {
            let mut cube_totals: HashMap<&str, i32> =
                HashMap::from([("red", 0), ("blue", 0), ("green", 0)]);
            let cube_sets: Vec<_> = set.split(", ").collect();
            for cube in cube_sets.iter() {
                let cubesplit: Vec<_> = cube.split(" ").collect();
                let amount: i32 = cubesplit[0].parse().unwrap();
                let color = cubesplit[1];

                let current_amount = cube_totals.get(&color).cloned().unwrap_or(0);
                cube_totals.insert(color, current_amount + amount);
            }
            for (key, value) in cube_totals.into_iter() {
                if key == "red" {
                    mr = cmp::max(mr, value);
                } else if key == "blue" {
                    mb = cmp::max(mb, value);
                } else if key == "green" {
                    mg = cmp::max(mg, value);
                }
            }
        }
        total += mr * mb * mg;
    }
    println!("Answer: {}", total);
}
