pub(crate) struct Cell {
    pub(crate) x: i32, pub(crate) y: i32, pub(crate) is_alive: bool}
trait Live_Dead {
    fn vital_sign (&self) -> bool;
}
impl Cell {
}
