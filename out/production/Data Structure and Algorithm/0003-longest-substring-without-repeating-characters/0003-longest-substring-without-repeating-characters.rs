use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        if s.is_empty() {
        return 0;
        }

        let mut map: HashMap<char, usize> = HashMap::new();
        let mut max_len = 0;
        let mut j = 0;

        for (i, ch) in s.chars().enumerate() {
            if let Some(&last_seen_index) = map.get(&ch) {
                if last_seen_index >= j {
                    j = last_seen_index + 1;
                }
            }

            map.insert(ch, i);

            let current_window_size = i - j + 1;

            if current_window_size > max_len {
            max_len = current_window_size;
            }
        }

        max_len as i32
    }
}