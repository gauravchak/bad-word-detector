use std::collections::HashMap;

struct SwearDetector {
  subs: &HashMap<char, char>,
  badwords: &Vec<String>,
}

impl SwearDetector {
    fn new (subs: &HashMap<char, char>, badwords: &Vec<String>) -> SwearDetector {
        SwearDetector { 
          subs: subs, 
          badwords: badwords 
        }
    }

    fn is_unsafe(&self, str:String) -> bool {
      // code goes here
      return false;
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
      let mut badwords:Vec<String> = vec!["hello"];
      let mut subs:HashMap<char, char> = HashMap::new();
      let my_detector = SwearDetector::new(subs, badwords);
      
      let x = String::from("hello");
      let res = my_detector.is_unsafe(x);
      let expected = true;
      assert_eq!(res, expected);
    }
}

