use std::collections::HashMap;

fn length_of_longest_substring(s: &str) -> usize {
    let mut map: HashMap<char, usize> = HashMap::new();
    let (mut start, mut max_len) = (0usize, 0usize);
    for (i, c) in s.chars().enumerate() {
        if let Some(&prev) = map.get(&c) {
            if prev >= start {
                start = prev + 1;
            }
        }
        map.insert(c, i);
        max_len = max_len.max(i - start + 1);
    }
    max_len
}

fn main() {
    let test = "abrkaabcdefghijjkkxyz";
    println!("Longest unique substring length: {}", length_of_longest_substring(test));
}
