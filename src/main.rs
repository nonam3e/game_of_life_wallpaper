// use std::cell::Cell;
mod settings;
mod cell;
mod drawing;

fn main() {
    let a = settings::Game_type::classic;
    let first_cell = cell::Cell{x: 0,y: 0, is_alive: true};
    println!("Hello, world!");

}
