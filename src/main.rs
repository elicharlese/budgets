use std::io;

fn main() {
    println!("Please input your api key.");

    let mut api_key = String::new();

    io::stdin()
        .read_line(&mut api_key)
        .expect("Failed to read line");

    println!("You guessed: {api_key}");
}