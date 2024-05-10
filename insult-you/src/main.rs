use std::io; 
fn main () {
    println!("1. ");
    println!("2. ");
   println!("Please input your option");
   let mut option = String::new();
    // We need to use the libary we just added
    io::stdin()
        .read_line(&mut option)
            .expect("DEATH");
let option: u32 = match option.trim().parse() {
    Ok(num) => num,
    Err(_) => {
        println!("Invalid");
        return;

    }
};
println!("Your input {}", option);
}
