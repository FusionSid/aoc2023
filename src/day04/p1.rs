use std::collections::HashSet;
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

    for line in data.iter() {
        let parts: Vec<&str> = line.trim_start_matches("Card ").split(": ").collect();
        let (winning_numbers, my_numbers): (Vec<i32>, Vec<i32>) = parts[1]
            .split(" | ") // the next like 10 lines are not written by me
            .map(|x| {
                x.split_whitespace()
                    .map(|num| num.parse().unwrap())
                    .collect()
            })
            .fold((Vec::new(), Vec::new()), |(mut win, mut my), nums| {
                if win.is_empty() {
                    win = nums;
                } else {
                    my = nums;
                }
                (win, my)
            });

        let winning_numbers_set: HashSet<i32> = winning_numbers.into_iter().collect();
        let my_numbers_set: HashSet<i32> = my_numbers.into_iter().collect();

        let intersection: HashSet<_> = winning_numbers_set
            .intersection(&my_numbers_set)
            .cloned()
            .collect();
        if intersection.len() != 0 {
            let exp = (intersection.len() - 1) as u32;
            total += i32::pow(2, exp);
        }
    }

    println!("Answer: {}", total);
}
