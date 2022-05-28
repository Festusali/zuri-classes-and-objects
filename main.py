class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name:str, age:int, tracks:list, score:float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name:str):
      """Changes student's name."""
      self.name = name
    
    def change_age(self, age:int):
      """Changes student's age."""
      if type(age) == int:
        self.age = age
      else:
        print("Age must be an integer.")
      
    def add_track(self, track:str):
      """Appends to student's track."""
      self.tracks.append(track)
      
    def get_score(self) -> float:
      """Returns student's score."""
      return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())
