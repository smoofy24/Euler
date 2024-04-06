
use num_traits::Float;
const LIMIT: i32 = 1000;

fn fract_to_int(num: f64) -> i64 {
    while num.fract() != 0.0 {
        let num = num * 10.0;
    }
    return num as i64;
}

fn main() {
    let fraction: f32 = 3.14;
    println!("{}",fract_to_int(fraction.fract() as f64));
}
