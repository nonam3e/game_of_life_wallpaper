// use std::cell::Cell;
// mod settings;
// mod cell;
// mod drawing;
// mod field;

fn main() {
    // let a = settings::Game_type::classic;
    // let first_cell = cell::Cell{x: 0,y: 0, is_alive: true};
    let display_width = 1920;
    let  display_height = 1080;
    let cell_size = 6;
    let field_width = display_width/cell_size;
    let field_height = display_height/cell_size;
    let mut field:Vec<Vec<u8>> = vec![vec![0; field_width];field_height];
    for i in 0..field_width {
        for j in 0..field_height {
            let sum = field[(field_width+i-1)%field_width][j] + field[(i+1)%field_width][j] + field[i][(j+1)%field_width] + field[i][(field_width+j-1)%field_width]
                + field [(i+1)%field_width][(j+1)%field_width] + field[(i+1)%field_width][(field_width+j-1)%field_width] + field[(field_width+i-1)%field_width][(j+1)%field_width] + field[(field_width+i-1)%field_width][(field_width+j-1)%field_width];
            field[i][j] = if field[i][j] == 0 && sum == 3 || field[i][j] == 1 && (sum == 2 || sum == 3) { 1 }
                                                        else{ 0 };

        }
    }

}