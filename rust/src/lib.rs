use std::collections::HashMap;

struct SwearDetector {
  subs: HashMap<char, char>,
  badwords: Vec<String>,
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
