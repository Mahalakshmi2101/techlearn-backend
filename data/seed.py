import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal, engine
import models

# Pre-hashed value of "password123" — avoids bcrypt version conflicts at seed time
HASHED_PASSWORD = "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

courses_data = [
    {
        "title": "Java Programming Fundamentals",
        "description": "Master the core concepts of Java — OOP, collections, exception handling, and more. Built for beginners who want a strong foundation before moving to frameworks.",
        "category": "Programming",
        "difficulty": "Beginner",
        "thumbnail": "java",
        "duration": "6 hours",
        "instructor": "Ravi Kumar",
        "lessons": [
            ("Introduction to Java & JVM", "Java is a class-based, object-oriented programming language designed to have as few implementation dependencies as possible. The JVM (Java Virtual Machine) is what makes Java platform-independent — your code compiles to bytecode, not machine code, and the JVM runs that bytecode on any OS.\n\nKey concepts:\n- JDK: Java Development Kit (compiler + tools)\n- JRE: Java Runtime Environment (runs Java programs)\n- JVM: Java Virtual Machine (executes bytecode)\n\nYour first program:\n```java\npublic class Hello {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}\n```\nEvery Java program starts from `main`. The class name must match the filename.", "15 min"),
            ("Data Types, Variables & Operators", "Java is statically typed — every variable must declare its type.\n\nPrimitive types:\n- int (32-bit integer)\n- long (64-bit integer)\n- double (64-bit float)\n- boolean (true/false)\n- char (single character)\n- byte, short, float\n\nReference types: String, arrays, objects\n\n```java\nint age = 21;\ndouble gpa = 9.0;\nboolean isPlaced = false;\nString name = \"Maha\";\n```\n\nOperators: arithmetic (+,-,*,/,%), relational (==,!=,<,>), logical (&&,||,!), assignment (=,+=,-=).", "20 min"),
            ("Control Flow — if, switch, loops", "Control flow determines the order in which statements execute.\n\nif-else:\n```java\nif (score >= 90) {\n    System.out.println(\"A grade\");\n} else if (score >= 75) {\n    System.out.println(\"B grade\");\n} else {\n    System.out.println(\"Below B\");\n}\n```\n\nfor loop:\n```java\nfor (int i = 0; i < 5; i++) {\n    System.out.println(i);\n}\n```\n\nwhile loop:\n```java\nint i = 0;\nwhile (i < 5) {\n    System.out.println(i++);\n}\n```\n\nswitch (Java 14+ arrow syntax):\n```java\nswitch (day) {\n    case \"Mon\" -> System.out.println(\"Start of week\");\n    case \"Fri\" -> System.out.println(\"End of week\");\n    default   -> System.out.println(\"Midweek\");\n}\n```", "20 min"),
            ("Object-Oriented Programming", "OOP organises code around objects — instances of classes that bundle data (fields) and behaviour (methods).\n\nFour pillars:\n1. Encapsulation — hide internal state, expose via getters/setters\n2. Inheritance — child class extends parent class\n3. Polymorphism — same method name, different behaviour\n4. Abstraction — hide complexity, show only essentials\n\n```java\npublic class Animal {\n    private String name;\n    public Animal(String name) { this.name = name; }\n    public void speak() { System.out.println(name + \" makes a sound\"); }\n}\n\npublic class Dog extends Animal {\n    public Dog(String name) { super(name); }\n    @Override\n    public void speak() { System.out.println(\"Woof!\"); }\n}\n```", "30 min"),
            ("Collections Framework", "Java Collections provide ready-made data structures.\n\nCommon ones:\n- ArrayList: dynamic array, ordered, allows duplicates\n- LinkedList: doubly linked list, fast insert/delete\n- HashMap: key-value pairs, O(1) average lookup\n- HashSet: unique elements, unordered\n- TreeMap: sorted key-value pairs\n\n```java\nArrayList<String> list = new ArrayList<>();\nlist.add(\"Java\");\nlist.add(\"Python\");\nlist.remove(\"Python\");\n\nHashMap<String, Integer> scores = new HashMap<>();\nscores.put(\"Alice\", 95);\nscores.put(\"Bob\", 88);\nSystem.out.println(scores.get(\"Alice\")); // 95\n```\n\nIterating with for-each:\n```java\nfor (String item : list) {\n    System.out.println(item);\n}\n```", "25 min"),
        ],
        "quiz": {
            "title": "Java Fundamentals Quiz",
            "time_limit": 600,
            "questions": [
                ("What does JVM stand for?", "Java Virtual Memory", "Java Virtual Machine", "Java Variable Method", "Java Verified Module", "b", "JVM stands for Java Virtual Machine. It executes Java bytecode and provides platform independence."),
                ("Which is NOT a primitive type in Java?", "int", "boolean", "String", "char", "c", "String is a reference type (class), not a primitive. The 8 primitives are: byte, short, int, long, float, double, boolean, char."),
                ("What is the output of: System.out.println(10 / 3)?", "3.33", "3", "4", "3.0", "b", "Integer division in Java truncates the decimal. 10/3 = 3 (not 3.33). Use 10.0/3 for decimal result."),
                ("Which collection allows duplicate elements?", "HashSet", "TreeSet", "ArrayList", "LinkedHashSet", "c", "ArrayList allows duplicates and maintains insertion order. Sets (HashSet, TreeSet, LinkedHashSet) do not allow duplicates."),
                ("What keyword is used to inherit a class in Java?", "implements", "inherits", "extends", "super", "c", "extends is used for class inheritance. implements is used for interfaces."),
            ]
        }
    },
    {
        "title": "Data Structures & Algorithms",
        "description": "Arrays, linked lists, stacks, queues, trees, graphs, and essential algorithms. Placement-focused — every topic maps directly to interview questions at TCS, Wipro, Infosys, and product companies.",
        "category": "DSA",
        "difficulty": "Intermediate",
        "thumbnail": "dsa",
        "duration": "8 hours",
        "instructor": "Priya Sharma",
        "lessons": [
            ("Arrays & Strings", "An array is a contiguous block of memory storing elements of the same type. Access is O(1) by index, insertion/deletion is O(n).\n\nKey operations:\n```java\nint[] arr = {3, 1, 4, 1, 5};\nArrays.sort(arr);\nint idx = Arrays.binarySearch(arr, 4);\nint[] copy = Arrays.copyOf(arr, arr.length);\n```\n\nTwo-pointer technique:\n```java\nint left = 0, right = arr.length - 1;\nwhile (left < right) {\n    int sum = arr[left] + arr[right];\n    if (sum == target) return true;\n    else if (sum < target) left++;\n    else right--;\n}\n```", "30 min"),
            ("Linked Lists", "A linked list is a chain of nodes where each node holds data and a pointer to the next node.\n\nReverse a linked list:\n```java\nNode prev = null, curr = head;\nwhile (curr != null) {\n    Node next = curr.next;\n    curr.next = prev;\n    prev = curr;\n    curr = next;\n}\nhead = prev;\n```\n\nDetect cycle — Floyd's algorithm:\n```java\nNode slow = head, fast = head;\nwhile (fast != null && fast.next != null) {\n    slow = slow.next;\n    fast = fast.next.next;\n    if (slow == fast) return true;\n}\nreturn false;\n```", "30 min"),
            ("Stacks & Queues", "Stack — LIFO. Queue — FIFO.\n\nStack:\n```java\nDeque<Integer> stack = new ArrayDeque<>();\nstack.push(1); stack.push(2);\nstack.pop();  // 2\n```\n\nQueue:\n```java\nQueue<Integer> queue = new LinkedList<>();\nqueue.offer(1); queue.offer(2);\nqueue.poll(); // 1\n```", "25 min"),
            ("Trees & Binary Search Trees", "BST property: left < node < right.\n\nInorder traversal:\n```java\nvoid inorder(TreeNode root) {\n    if (root == null) return;\n    inorder(root.left);\n    System.out.print(root.val + \" \");\n    inorder(root.right);\n}\n```", "35 min"),
            ("Sorting & Searching Algorithms", "Binary Search — O(log n):\n```java\nint binarySearch(int[] arr, int target) {\n    int left = 0, right = arr.length - 1;\n    while (left <= right) {\n        int mid = left + (right - left) / 2;\n        if (arr[mid] == target) return mid;\n        else if (arr[mid] < target) left = mid + 1;\n        else right = mid - 1;\n    }\n    return -1;\n}\n```", "30 min"),
        ],
        "quiz": {
            "title": "DSA Quiz",
            "time_limit": 600,
            "questions": [
                ("What is the time complexity of binary search?", "O(n)", "O(n log n)", "O(log n)", "O(1)", "c", "Binary search halves the search space each step, giving O(log n) time complexity. Array must be sorted."),
                ("Which data structure uses LIFO order?", "Queue", "Stack", "LinkedList", "Tree", "b", "Stack uses LIFO — Last In, First Out. The last element pushed is the first one popped."),
                ("What is the worst-case time complexity of Quick Sort?", "O(n log n)", "O(n)", "O(n²)", "O(log n)", "c", "Quick Sort's worst case is O(n²) when the pivot is always the smallest or largest element."),
                ("In a BST, inorder traversal gives elements in:", "Random order", "Descending order", "Level order", "Ascending order", "d", "Inorder traversal (left → root → right) of a BST always yields elements in ascending sorted order."),
                ("Floyd's cycle detection uses:", "One pointer", "Two pointers at same speed", "A slow and a fast pointer", "Three pointers", "c", "Floyd's algorithm uses a slow pointer (moves 1 step) and a fast pointer (moves 2 steps). If there's a cycle, they meet."),
            ]
        }
    },
    {
        "title": "Spring Boot & REST APIs",
        "description": "Build production-ready REST APIs with Spring Boot. Covers dependency injection, JPA, Spring Security basics, and best practices used in real industry projects.",
        "category": "Backend",
        "difficulty": "Intermediate",
        "thumbnail": "spring",
        "duration": "7 hours",
        "instructor": "Arjun Menon",
        "lessons": [
            ("Spring Boot Basics", "Spring Boot eliminates boilerplate configuration.\n\n```java\n@SpringBootApplication\npublic class App {\n    public static void main(String[] args) {\n        SpringApplication.run(App.class, args);\n    }\n}\n\n@RestController\n@RequestMapping(\"/api\")\npublic class HelloController {\n    @GetMapping(\"/hello\")\n    public String hello() {\n        return \"Hello from Spring Boot!\";\n    }\n}\n```", "25 min"),
            ("Dependency Injection & IoC", "Spring's IoC container manages beans and injects dependencies.\n\n```java\n@Service\npublic class CourseService {\n    private final CourseRepository repo;\n    public CourseService(CourseRepository repo) {\n        this.repo = repo;\n    }\n}\n```", "20 min"),
            ("Spring Data JPA", "JPA maps Java objects to database tables.\n\n```java\n@Entity\npublic class Course {\n    @Id\n    @GeneratedValue(strategy = GenerationType.IDENTITY)\n    private Long id;\n    private String title;\n}\n\npublic interface CourseRepository extends JpaRepository<Course, Long> {\n    List<Course> findByCategory(String category);\n}\n```", "30 min"),
            ("Building REST APIs", "REST uses HTTP methods for CRUD.\n\n```java\n@RestController\n@RequestMapping(\"/api/courses\")\npublic class CourseController {\n    @GetMapping\n    public ResponseEntity<List<Course>> getAll() {\n        return ResponseEntity.ok(service.getAllCourses());\n    }\n    @PostMapping\n    public ResponseEntity<Course> create(@RequestBody Course course) {\n        return ResponseEntity.status(201).body(service.createCourse(course));\n    }\n}\n```", "30 min"),
            ("Exception Handling & Validation", "Global exception handling with @ControllerAdvice.\n\n```java\n@RestControllerAdvice\npublic class GlobalExceptionHandler {\n    @ExceptionHandler(ResourceNotFoundException.class)\n    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {\n        return ResponseEntity.status(404).body(new ErrorResponse(404, ex.getMessage()));\n    }\n}\n```", "25 min"),
        ],
        "quiz": {
            "title": "Spring Boot Quiz",
            "time_limit": 600,
            "questions": [
                ("What does @RestController do?", "Marks a class as a service", "Combines @Controller and @ResponseBody", "Creates a database connection", "Handles exceptions globally", "b", "@RestController combines @Controller and @ResponseBody so every method returns data directly."),
                ("Which HTTP method is used to CREATE a resource?", "GET", "PUT", "DELETE", "POST", "d", "POST is used to create a new resource."),
                ("What is Inversion of Control (IoC)?", "The developer controls all object creation", "The framework controls object creation and injection", "A loop that runs forever", "A type of database transaction", "b", "IoC means the Spring container creates and manages objects and injects dependencies."),
                ("Which annotation marks a class for data access layer?", "@Service", "@Component", "@Controller", "@Repository", "d", "@Repository marks a class as a data access component."),
                ("What does JpaRepository provide?", "Only findById method", "CRUD methods + paging + sorting out of the box", "Only save and delete", "HTTP request handling", "b", "JpaRepository gives you findAll, findById, save, delete, and pagination methods without writing any code."),
            ]
        }
    },
    {
        "title": "React & Frontend Development",
        "description": "Modern frontend development with React. Hooks, state management, API integration, and building UIs that actually work. Practical and project-focused.",
        "category": "Frontend",
        "difficulty": "Intermediate",
        "thumbnail": "react",
        "duration": "6 hours",
        "instructor": "Sneha Patel",
        "lessons": [
            ("React Fundamentals & JSX", "React uses a component-based architecture.\n\n```jsx\nfunction Welcome({ name }) {\n    return (\n        <div className=\"card\">\n            <h1>Hello, {name}!</h1>\n        </div>\n    );\n}\n```", "20 min"),
            ("useState & useEffect Hooks", "```jsx\nconst [count, setCount] = useState(0);\n\nuseEffect(() => {\n    fetchCourse(courseId);\n}, [courseId]);\n```", "25 min"),
            ("API Integration with Axios", "```jsx\nuseEffect(() => {\n    api.get('/courses/')\n        .then(res => setCourses(res.data))\n        .catch(err => setError(err.message))\n        .finally(() => setLoading(false));\n}, []);\n```", "25 min"),
            ("React Router & Navigation", "```jsx\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\n\nfunction App() {\n    return (\n        <BrowserRouter>\n            <Routes>\n                <Route path=\"/\" element={<CourseList />} />\n                <Route path=\"/course/:id\" element={<CourseDetail />} />\n            </Routes>\n        </BrowserRouter>\n    );\n}\n```", "20 min"),
            ("State Management & Context API", "```jsx\nconst AuthContext = createContext();\n\nexport function AuthProvider({ children }) {\n    const [user, setUser] = useState(null);\n    return (\n        <AuthContext.Provider value={{ user }}>\n            {children}\n        </AuthContext.Provider>\n    );\n}\n```", "25 min"),
        ],
        "quiz": {
            "title": "React Quiz",
            "time_limit": 600,
            "questions": [
                ("What hook manages local state in a function component?", "useEffect", "useContext", "useRef", "useState", "d", "useState returns a state value and a setter function."),
                ("When does useEffect with an empty dependency array [] run?", "On every render", "Only when state changes", "Only on mount (once)", "Never", "c", "Empty dependency array means the effect runs once after the initial render."),
                ("What is JSX?", "A new programming language", "A database query language", "JavaScript XML — HTML-like syntax in JS files", "A CSS preprocessor", "c", "JSX is a syntax extension for JavaScript that looks like HTML."),
                ("How do you pass data to a child component?", "Through state", "Through props", "Through context only", "Through the DOM", "b", "Props are how parent components pass data to children."),
                ("What does useNavigate() do?", "Fetches data from an API", "Manages form state", "Enables programmatic navigation between routes", "Creates context", "c", "useNavigate returns a function that lets you navigate programmatically."),
            ]
        }
    },
    {
        "title": "SQL & Database Design",
        "description": "Write SQL that actually works under pressure. Joins, subqueries, indexing, normalization, and the database design decisions that separate good engineers from great ones.",
        "category": "Database",
        "difficulty": "Beginner",
        "thumbnail": "sql",
        "duration": "5 hours",
        "instructor": "Divya Nair",
        "lessons": [
            ("SQL Basics & CRUD", "```sql\nINSERT INTO students (name, email, gpa) VALUES ('Maha', 'maha@email.com', 9.0);\nSELECT name, gpa FROM students WHERE gpa > 8.5;\nUPDATE students SET gpa = 9.2 WHERE name = 'Maha';\nDELETE FROM students WHERE id = 5;\n```", "20 min"),
            ("Joins", "```sql\nSELECT s.name, c.title\nFROM students s\nINNER JOIN enrollments e ON s.id = e.student_id\nINNER JOIN courses c ON e.course_id = c.id;\n```", "25 min"),
            ("Aggregations & GROUP BY", "```sql\nSELECT department, AVG(gpa) AS avg_gpa\nFROM students\nGROUP BY department\nHAVING AVG(gpa) > 8.0;\n```", "20 min"),
            ("Indexes & Performance", "```sql\nCREATE INDEX idx_students_email ON students(email);\nEXPLAIN SELECT * FROM students WHERE email = 'maha@email.com';\n```", "25 min"),
            ("Database Design & Normalization", "1NF, 2NF, 3NF — eliminate redundancy and ensure data integrity.\n\n```sql\nCREATE TABLE customers (\n    id INT PRIMARY KEY,\n    name VARCHAR(100),\n    email VARCHAR(100) UNIQUE\n);\nCREATE TABLE orders (\n    id INT PRIMARY KEY,\n    customer_id INT REFERENCES customers(id),\n    product VARCHAR(100),\n    price DECIMAL(10,2)\n);\n```", "25 min"),
        ],
        "quiz": {
            "title": "SQL Quiz",
            "time_limit": 600,
            "questions": [
                ("Which JOIN returns only rows that have matches in BOTH tables?", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "FULL JOIN", "c", "INNER JOIN returns only the intersection — rows where the join condition is satisfied in both tables."),
                ("What is the difference between WHERE and HAVING?", "No difference", "WHERE filters before grouping, HAVING filters after", "HAVING filters before grouping, WHERE filters after", "WHERE works only with joins", "b", "WHERE filters individual rows before GROUP BY. HAVING filters the groups after aggregation."),
                ("What does an index do?", "Slows down reads but speeds up writes", "Speeds up reads at the cost of write speed and storage", "Encrypts the column data", "Ensures uniqueness", "b", "Indexes speed up SELECT queries by avoiding full table scans."),
                ("Which normal form eliminates transitive dependencies?", "1NF", "2NF", "3NF", "BCNF", "c", "3NF requires that non-key columns depend only on the primary key."),
                ("What does COUNT(*) return?", "Sum of all values", "Number of non-null values in a column", "Total number of rows (including NULLs)", "Average value", "c", "COUNT(*) counts all rows including those with NULL values."),
            ]
        }
    },
]


def seed():
    db.query(models.LessonCompletion).delete()
    db.query(models.QuizResult).delete()
    db.query(models.UserProgress).delete()
    db.query(models.Question).delete()
    db.query(models.Quiz).delete()
    db.query(models.Lesson).delete()
    db.query(models.Course).delete()
    db.query(models.User).delete()
    db.commit()

    test_user = models.User(
        username="Bob",
        email="bob@techlearn.com",
        hashed_password=HASHED_PASSWORD
    )
    
    db.add(test_user)
    db.commit()

    for course_data in courses_data:
        course = models.Course(
            title=course_data["title"],
            description=course_data["description"],
            category=course_data["category"],
            difficulty=course_data["difficulty"],
            thumbnail=course_data["thumbnail"],
            duration=course_data["duration"],
            instructor=course_data["instructor"],
        )
        db.add(course)
        db.flush()

        for order, (title, content, duration) in enumerate(course_data["lessons"], 1):
            lesson = models.Lesson(
                course_id=course.id,
                title=title,
                content=content,
                order=order,
                duration=duration,
            )
            db.add(lesson)

        qd = course_data["quiz"]
        quiz = models.Quiz(
            course_id=course.id,
            title=qd["title"],
            time_limit=qd["time_limit"],
        )
        db.add(quiz)
        db.flush()

        for text, a, b, c, d, correct, explanation in qd["questions"]:
            question = models.Question(
                quiz_id=quiz.id,
                text=text,
                option_a=a,
                option_b=b,
                option_c=c,
                option_d=d,
                correct_option=correct,
                explanation=explanation,
            )
            db.add(question)

    db.commit()
    print("✅ Database seeded successfully.")
    db.close()


if __name__ == "__main__":
    seed()