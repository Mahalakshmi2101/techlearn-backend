import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal, engine
import models

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
            ("Arrays & Strings", "An array is a contiguous block of memory storing elements of the same type. Access is O(1) by index, insertion/deletion is O(n).\n\nKey operations:\n```java\nint[] arr = {3, 1, 4, 1, 5};\nArrays.sort(arr);                    // sort\nint idx = Arrays.binarySearch(arr, 4); // binary search\nint[] copy = Arrays.copyOf(arr, arr.length); // copy\n```\n\nString tricks:\n```java\nString s = \"hello\";\ns.length()        // 5\ns.charAt(0)       // 'h'\ns.substring(1, 3) // \"el\"\ns.indexOf('l')    // 2\ns.reverse()       // use StringBuilder\nnew StringBuilder(s).reverse().toString(); // \"olleh\"\n```\n\nTwo-pointer technique — find pair with target sum:\n```java\nint left = 0, right = arr.length - 1;\nwhile (left < right) {\n    int sum = arr[left] + arr[right];\n    if (sum == target) return true;\n    else if (sum < target) left++;\n    else right--;\n}\n```", "30 min"),
            ("Linked Lists", "A linked list is a chain of nodes where each node holds data and a pointer to the next node. Unlike arrays, nodes are not contiguous in memory.\n\nNode structure:\n```java\nclass Node {\n    int data;\n    Node next;\n    Node(int data) { this.data = data; }\n}\n```\n\nOperations:\n- Insert at head: O(1)\n- Insert at tail: O(n) without tail pointer\n- Delete: O(n) to find, O(1) to remove\n- Search: O(n)\n\nReverse a linked list (must-know):\n```java\nNode prev = null, curr = head;\nwhile (curr != null) {\n    Node next = curr.next;\n    curr.next = prev;\n    prev = curr;\n    curr = next;\n}\nhead = prev;\n```\n\nDetect cycle — Floyd's algorithm:\n```java\nNode slow = head, fast = head;\nwhile (fast != null && fast.next != null) {\n    slow = slow.next;\n    fast = fast.next.next;\n    if (slow == fast) return true; // cycle\n}\nreturn false;\n```", "30 min"),
            ("Stacks & Queues", "Stack — LIFO (Last In, First Out). Think: undo history, browser back button, function call stack.\n\nQueue — FIFO (First In, First Out). Think: printer queue, BFS traversal.\n\nStack with Java:\n```java\nDeque<Integer> stack = new ArrayDeque<>();\nstack.push(1); stack.push(2); stack.push(3);\nstack.pop();   // 3\nstack.peek();  // 2 (no removal)\n```\n\nQueue with Java:\n```java\nQueue<Integer> queue = new LinkedList<>();\nqueue.offer(1); queue.offer(2); queue.offer(3);\nqueue.poll();   // 1\nqueue.peek();   // 2\n```\n\nBalanced parentheses (classic stack problem):\n```java\nDeque<Character> stack = new ArrayDeque<>();\nfor (char c : s.toCharArray()) {\n    if (c == '(') stack.push(c);\n    else if (stack.isEmpty()) return false;\n    else stack.pop();\n}\nreturn stack.isEmpty();\n```", "25 min"),
            ("Trees & Binary Search Trees", "A tree is a hierarchical data structure. Binary tree: each node has at most 2 children.\n\nBST property: left subtree < node < right subtree. This gives O(log n) search on balanced trees.\n\n```java\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int val) { this.val = val; }\n}\n```\n\nInorder traversal (gives sorted output for BST):\n```java\nvoid inorder(TreeNode root) {\n    if (root == null) return;\n    inorder(root.left);\n    System.out.print(root.val + \" \");\n    inorder(root.right);\n}\n```\n\nLevel-order traversal (BFS):\n```java\nQueue<TreeNode> q = new LinkedList<>();\nq.offer(root);\nwhile (!q.isEmpty()) {\n    TreeNode node = q.poll();\n    System.out.print(node.val + \" \");\n    if (node.left != null) q.offer(node.left);\n    if (node.right != null) q.offer(node.right);\n}\n```", "35 min"),
            ("Sorting & Searching Algorithms", "Must-know algorithms for placements:\n\nBubble Sort — O(n²): repeatedly swap adjacent elements\nSelection Sort — O(n²): find min, place at front\nInsertion Sort — O(n²) worst, O(n) best: build sorted array one element at a time\nMerge Sort — O(n log n): divide and conquer, stable\nQuick Sort — O(n log n) avg: pivot-based, in-place\n\nBinary Search — O(log n), array must be sorted:\n```java\nint binarySearch(int[] arr, int target) {\n    int left = 0, right = arr.length - 1;\n    while (left <= right) {\n        int mid = left + (right - left) / 2; // avoids overflow\n        if (arr[mid] == target) return mid;\n        else if (arr[mid] < target) left = mid + 1;\n        else right = mid - 1;\n    }\n    return -1;\n}\n```\n\nAlways use `left + (right - left) / 2` not `(left + right) / 2` — prevents integer overflow.", "30 min"),
        ],
        "quiz": {
            "title": "DSA Quiz",
            "time_limit": 600,
            "questions": [
                ("What is the time complexity of binary search?", "O(n)", "O(n log n)", "O(log n)", "O(1)", "c", "Binary search halves the search space each step, giving O(log n) time complexity. Array must be sorted."),
                ("Which data structure uses LIFO order?", "Queue", "Stack", "LinkedList", "Tree", "b", "Stack uses LIFO — Last In, First Out. The last element pushed is the first one popped."),
                ("What is the worst-case time complexity of Quick Sort?", "O(n log n)", "O(n)", "O(n²)", "O(log n)", "c", "Quick Sort's worst case is O(n²) when the pivot is always the smallest or largest element (already sorted array with bad pivot choice)."),
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
            ("Spring Boot Basics", "Spring Boot is an opinionated framework built on top of Spring that eliminates boilerplate configuration. It auto-configures most things so you can focus on business logic.\n\nKey annotations:\n- @SpringBootApplication: marks the entry point, enables auto-configuration\n- @RestController: marks class as REST controller, combines @Controller + @ResponseBody\n- @RequestMapping / @GetMapping / @PostMapping: maps HTTP requests to methods\n- @Autowired: dependency injection\n\n```java\n@SpringBootApplication\npublic class App {\n    public static void main(String[] args) {\n        SpringApplication.run(App.class, args);\n    }\n}\n\n@RestController\n@RequestMapping(\"/api\")\npublic class HelloController {\n    @GetMapping(\"/hello\")\n    public String hello() {\n        return \"Hello from Spring Boot!\";\n    }\n}\n```\n\nApplication runs on port 8080 by default. Change in application.properties:\n```\nserver.port=8081\n```", "25 min"),
            ("Dependency Injection & IoC", "Inversion of Control (IoC) means the framework controls object creation instead of your code. Spring's IoC container manages beans (objects) and injects dependencies.\n\nThree ways to inject:\n1. Constructor injection (recommended)\n2. Setter injection\n3. Field injection (@Autowired)\n\n```java\n@Service\npublic class CourseService {\n    private final CourseRepository repo;\n\n    // Constructor injection — preferred\n    public CourseService(CourseRepository repo) {\n        this.repo = repo;\n    }\n\n    public List<Course> getAllCourses() {\n        return repo.findAll();\n    }\n}\n```\n\nStereotype annotations:\n- @Component: generic bean\n- @Service: business logic layer\n- @Repository: data access layer\n- @Controller/@RestController: presentation layer", "20 min"),
            ("Spring Data JPA", "JPA (Java Persistence API) maps Java objects to database tables. Spring Data JPA makes this even simpler — you define an interface and Spring generates the SQL.\n\nEntity:\n```java\n@Entity\n@Table(name = \"courses\")\npublic class Course {\n    @Id\n    @GeneratedValue(strategy = GenerationType.IDENTITY)\n    private Long id;\n\n    @Column(nullable = false)\n    private String title;\n\n    private String description;\n}\n```\n\nRepository:\n```java\npublic interface CourseRepository extends JpaRepository<Course, Long> {\n    List<Course> findByCategory(String category);\n    List<Course> findByDifficultyOrderByTitleAsc(String difficulty);\n    // Spring generates the query from the method name!\n}\n```\n\napplication.properties:\n```\nspring.datasource.url=jdbc:mysql://localhost:3306/techlearn\nspring.datasource.username=root\nspring.datasource.password=yourpassword\nspring.jpa.hibernate.ddl-auto=update\n```", "30 min"),
            ("Building REST APIs", "REST (Representational State Transfer) uses HTTP methods to perform CRUD operations.\n\nHTTP methods:\n- GET: read data\n- POST: create data\n- PUT: update (full replacement)\n- PATCH: partial update\n- DELETE: delete\n\n```java\n@RestController\n@RequestMapping(\"/api/courses\")\npublic class CourseController {\n    private final CourseService service;\n\n    public CourseController(CourseService service) {\n        this.service = service;\n    }\n\n    @GetMapping\n    public ResponseEntity<List<Course>> getAll() {\n        return ResponseEntity.ok(service.getAllCourses());\n    }\n\n    @GetMapping(\"/{id}\")\n    public ResponseEntity<Course> getById(@PathVariable Long id) {\n        return ResponseEntity.ok(service.getCourseById(id));\n    }\n\n    @PostMapping\n    public ResponseEntity<Course> create(@RequestBody Course course) {\n        return ResponseEntity.status(201).body(service.createCourse(course));\n    }\n\n    @DeleteMapping(\"/{id}\")\n    public ResponseEntity<Void> delete(@PathVariable Long id) {\n        service.deleteCourse(id);\n        return ResponseEntity.noContent().build();\n    }\n}\n```", "30 min"),
            ("Exception Handling & Validation", "Global exception handling with @ControllerAdvice keeps your controllers clean.\n\n```java\n@RestControllerAdvice\npublic class GlobalExceptionHandler {\n\n    @ExceptionHandler(ResourceNotFoundException.class)\n    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {\n        return ResponseEntity.status(404)\n            .body(new ErrorResponse(404, ex.getMessage()));\n    }\n\n    @ExceptionHandler(Exception.class)\n    public ResponseEntity<ErrorResponse> handleGeneral(Exception ex) {\n        return ResponseEntity.status(500)\n            .body(new ErrorResponse(500, \"Internal server error\"));\n    }\n}\n```\n\nInput validation with @Valid:\n```java\npublic class CourseRequest {\n    @NotBlank(message = \"Title is required\")\n    @Size(min = 3, max = 100)\n    private String title;\n\n    @NotBlank\n    private String description;\n}\n\n@PostMapping\npublic ResponseEntity<Course> create(@Valid @RequestBody CourseRequest req) {\n    ...\n}\n```", "25 min"),
        ],
        "quiz": {
            "title": "Spring Boot Quiz",
            "time_limit": 600,
            "questions": [
                ("What does @RestController do?", "Marks a class as a service", "Combines @Controller and @ResponseBody", "Creates a database connection", "Handles exceptions globally", "b", "@RestController is a convenience annotation that combines @Controller and @ResponseBody, so every method returns data directly (not a view name)."),
                ("Which HTTP method is used to CREATE a resource?", "GET", "PUT", "DELETE", "POST", "d", "POST is used to create a new resource. GET reads, PUT updates/replaces, DELETE removes."),
                ("What is Inversion of Control (IoC)?", "The developer controls all object creation", "The framework controls object creation and injection", "A loop that runs forever", "A type of database transaction", "b", "IoC means the Spring container creates and manages objects (beans) and injects dependencies, instead of your code doing it manually."),
                ("Which annotation marks a class for data access layer?", "@Service", "@Component", "@Controller", "@Repository", "d", "@Repository marks a class as a data access component. It also enables Spring's exception translation for persistence exceptions."),
                ("What does JpaRepository provide?", "Only findById method", "CRUD methods + paging + sorting out of the box", "Only save and delete", "HTTP request handling", "b", "JpaRepository extends CrudRepository and PagingAndSortingRepository, giving you findAll, findById, save, delete, and pagination methods without writing any code."),
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
            ("React Fundamentals & JSX", "React is a JavaScript library for building user interfaces. It uses a component-based architecture — your UI is broken into reusable pieces.\n\nJSX (JavaScript XML) lets you write HTML-like syntax inside JavaScript:\n```jsx\nfunction Welcome({ name }) {\n    return (\n        <div className=\"card\">\n            <h1>Hello, {name}!</h1>\n            <p>Welcome to TechLearn.</p>\n        </div>\n    );\n}\n\n// Usage\n<Welcome name=\"Maha\" />\n```\n\nKey JSX rules:\n- className instead of class\n- All tags must be closed (<br /> not <br>)\n- Return a single root element (use <> fragment if needed)\n- JavaScript expressions go in {}\n- Events: onClick, onChange (camelCase)", "20 min"),
            ("useState & useEffect Hooks", "Hooks let function components use state and lifecycle features.\n\nuseState — local component state:\n```jsx\nconst [count, setCount] = useState(0);\nconst [user, setUser] = useState(null);\nconst [loading, setLoading] = useState(true);\n\n// Update state\nsetCount(count + 1);\nsetCount(prev => prev + 1); // safer with previous value\n```\n\nuseEffect — side effects (API calls, subscriptions, timers):\n```jsx\n// Runs on every render\nuseEffect(() => { ... });\n\n// Runs only on mount\nuseEffect(() => { ... }, []);\n\n// Runs when dependency changes\nuseEffect(() => {\n    fetchCourse(courseId);\n}, [courseId]);\n\n// Cleanup (timers, subscriptions)\nuseEffect(() => {\n    const timer = setInterval(() => setTime(t => t - 1), 1000);\n    return () => clearInterval(timer); // cleanup\n}, []);\n```", "25 min"),
            ("API Integration with Axios", "Fetching data from a backend API is core to any real app.\n\nSetup:\n```bash\nnpm install axios\n```\n\nCreate an axios instance with base URL and auth:\n```js\n// api/axios.js\nimport axios from 'axios';\n\nconst api = axios.create({\n    baseURL: 'http://localhost:8000',\n});\n\n// Auto-attach JWT token\napi.interceptors.request.use(config => {\n    const token = localStorage.getItem('token');\n    if (token) config.headers.Authorization = `Bearer ${token}`;\n    return config;\n});\n\nexport default api;\n```\n\nUsage in component:\n```jsx\nconst [courses, setCourses] = useState([]);\nconst [loading, setLoading] = useState(true);\nconst [error, setError] = useState(null);\n\nuseEffect(() => {\n    api.get('/courses/')\n        .then(res => setCourses(res.data))\n        .catch(err => setError(err.message))\n        .finally(() => setLoading(false));\n}, []);\n\nif (loading) return <Spinner />;\nif (error) return <ErrorState message={error} />;\nif (!courses.length) return <EmptyState />;\n```", "25 min"),
            ("React Router & Navigation", "React Router enables client-side navigation without page reloads.\n\n```bash\nnpm install react-router-dom\n```\n\nSetup:\n```jsx\nimport { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';\n\nfunction App() {\n    return (\n        <BrowserRouter>\n            <Routes>\n                <Route path=\"/\" element={<CourseList />} />\n                <Route path=\"/course/:id\" element={<CourseDetail />} />\n                <Route path=\"/login\" element={<Login />} />\n                <Route path=\"*\" element={<Navigate to=\"/\" />} />\n            </Routes>\n        </BrowserRouter>\n    );\n}\n```\n\nNavigating:\n```jsx\nimport { useNavigate, useParams, Link } from 'react-router-dom';\n\n// Programmatic navigation\nconst navigate = useNavigate();\nnavigate('/course/1');\nnavigate(-1); // go back\n\n// URL params\nconst { id } = useParams(); // from /course/:id\n\n// Link component (no page reload)\n<Link to=\"/course/1\">View Course</Link>\n```", "20 min"),
            ("State Management & Context API", "When multiple components need the same data, prop drilling becomes messy. Context API solves this.\n\n```jsx\n// AuthContext.jsx\nconst AuthContext = createContext();\n\nexport function AuthProvider({ children }) {\n    const [user, setUser] = useState(null);\n    const [token, setToken] = useState(localStorage.getItem('token'));\n\n    const login = (userData, accessToken) => {\n        setUser(userData);\n        setToken(accessToken);\n        localStorage.setItem('token', accessToken);\n    };\n\n    const logout = () => {\n        setUser(null);\n        setToken(null);\n        localStorage.removeItem('token');\n    };\n\n    return (\n        <AuthContext.Provider value={{ user, token, login, logout }}>\n            {children}\n        </AuthContext.Provider>\n    );\n}\n\nexport const useAuth = () => useContext(AuthContext);\n\n// Usage anywhere\nconst { user, login, logout } = useAuth();\n```", "25 min"),
        ],
        "quiz": {
            "title": "React Quiz",
            "time_limit": 600,
            "questions": [
                ("What hook manages local state in a function component?", "useEffect", "useContext", "useRef", "useState", "d", "useState returns a state value and a setter function. Call the setter to update state and trigger a re-render."),
                ("When does useEffect with an empty dependency array [] run?", "On every render", "Only when state changes", "Only on mount (once)", "Never", "c", "Empty dependency array [] means the effect runs once after the initial render — equivalent to componentDidMount in class components."),
                ("What is JSX?", "A new programming language", "A database query language", "JavaScript XML — HTML-like syntax in JS files", "A CSS preprocessor", "c", "JSX is a syntax extension for JavaScript that looks like HTML. Babel compiles it to React.createElement() calls."),
                ("How do you pass data to a child component?", "Through state", "Through props", "Through context only", "Through the DOM", "b", "Props (properties) are how parent components pass data to children. They are read-only in the child."),
                ("What does useNavigate() do?", "Fetches data from an API", "Manages form state", "Enables programmatic navigation between routes", "Creates context", "c", "useNavigate returns a function that lets you navigate programmatically — useful after form submissions, login/logout, etc."),
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
            ("SQL Basics & CRUD", "SQL (Structured Query Language) is how you talk to relational databases. Every web application uses it.\n\nCRUD operations:\n```sql\n-- CREATE\nINSERT INTO students (name, email, gpa)\nVALUES ('Maha', 'maha@email.com', 9.0);\n\n-- READ\nSELECT name, gpa FROM students WHERE gpa > 8.5;\nSELECT * FROM students ORDER BY gpa DESC LIMIT 10;\n\n-- UPDATE\nUPDATE students SET gpa = 9.2 WHERE name = 'Maha';\n\n-- DELETE\nDELETE FROM students WHERE id = 5;\n```\n\nFiltering:\n```sql\nWHERE age BETWEEN 20 AND 25\nWHERE name LIKE 'M%'        -- starts with M\nWHERE city IN ('Chennai', 'Mumbai')\nWHERE email IS NOT NULL\n```", "20 min"),
            ("Joins", "Joins combine rows from two or more tables based on a related column.\n\nTypes:\n- INNER JOIN: only matching rows from both tables\n- LEFT JOIN: all rows from left + matching from right (NULL if no match)\n- RIGHT JOIN: all rows from right + matching from left\n- FULL JOIN: all rows from both tables\n\n```sql\n-- Students with their enrolled courses\nSELECT s.name, c.title\nFROM students s\nINNER JOIN enrollments e ON s.id = e.student_id\nINNER JOIN courses c ON e.course_id = c.id;\n\n-- All students, even those not enrolled\nSELECT s.name, c.title\nFROM students s\nLEFT JOIN enrollments e ON s.id = e.student_id\nLEFT JOIN courses c ON e.course_id = c.id;\n```\n\nRemember: INNER JOIN = only intersection. LEFT JOIN = all from left side, matched or not.", "25 min"),
            ("Aggregations & GROUP BY", "Aggregate functions compute values across multiple rows.\n\nFunctions: COUNT, SUM, AVG, MAX, MIN\n\n```sql\n-- Count students per city\nSELECT city, COUNT(*) AS student_count\nFROM students\nGROUP BY city\nORDER BY student_count DESC;\n\n-- Average GPA per department\nSELECT department, AVG(gpa) AS avg_gpa\nFROM students\nGROUP BY department\nHAVING AVG(gpa) > 8.0;  -- filter on aggregated result\n```\n\nWHERE vs HAVING:\n- WHERE filters rows BEFORE grouping\n- HAVING filters groups AFTER grouping\n\n```sql\nSELECT department, COUNT(*) as count\nFROM students\nWHERE gpa > 7.0          -- filter individual rows first\nGROUP BY department\nHAVING COUNT(*) > 10;    -- then filter groups\n```", "20 min"),
            ("Indexes & Performance", "An index is a data structure (usually B-tree) that speeds up data retrieval at the cost of write speed and storage.\n\nWithout index: full table scan O(n)\nWith index: B-tree lookup O(log n)\n\n```sql\n-- Create index\nCREATE INDEX idx_students_email ON students(email);\nCREATE INDEX idx_composite ON orders(user_id, created_at);\n\n-- Drop index\nDROP INDEX idx_students_email ON students;\n\n-- See query execution plan\nEXPLAIN SELECT * FROM students WHERE email = 'maha@email.com';\n```\n\nWhen to index:\n✅ Columns used in WHERE, JOIN ON, ORDER BY\n✅ Foreign keys\n✅ High-cardinality columns (email, ID)\n\nWhen NOT to:\n❌ Small tables (full scan is faster)\n❌ Columns updated very frequently\n❌ Low-cardinality columns (gender, boolean)", "25 min"),
            ("Database Design & Normalization", "Normalization eliminates redundancy and ensures data integrity.\n\n1NF: atomic values, no repeating groups\n2NF: 1NF + no partial dependencies (non-key columns depend on WHOLE primary key)\n3NF: 2NF + no transitive dependencies (non-key columns depend only on primary key)\n\nBad design (not normalized):\n| order_id | customer_name | customer_email | product | price |\n|---|---|---|---|---|\n| 1 | Maha | m@e.com | Java Book | 500 |\n| 2 | Maha | m@e.com | DSA Book | 400 |\n\nProblem: customer data duplicated. If email changes, update multiple rows.\n\nNormalized:\n```sql\nCREATE TABLE customers (\n    id INT PRIMARY KEY,\n    name VARCHAR(100),\n    email VARCHAR(100) UNIQUE\n);\n\nCREATE TABLE orders (\n    id INT PRIMARY KEY,\n    customer_id INT REFERENCES customers(id),\n    product VARCHAR(100),\n    price DECIMAL(10,2)\n);\n```", "25 min"),
        ],
        "quiz": {
            "title": "SQL Quiz",
            "time_limit": 600,
            "questions": [
                ("Which JOIN returns only rows that have matches in BOTH tables?", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "FULL JOIN", "c", "INNER JOIN returns only the intersection — rows where the join condition is satisfied in both tables."),
                ("What is the difference between WHERE and HAVING?", "No difference", "WHERE filters before grouping, HAVING filters after", "HAVING filters before grouping, WHERE filters after", "WHERE works only with joins", "b", "WHERE filters individual rows before GROUP BY. HAVING filters the groups after aggregation. Use HAVING with aggregate functions like COUNT, AVG."),
                ("What does an index do?", "Slows down reads but speeds up writes", "Speeds up reads at the cost of write speed and storage", "Encrypts the column data", "Ensures uniqueness", "b", "Indexes (usually B-trees) speed up SELECT/WHERE queries by avoiding full table scans. They add overhead to INSERT/UPDATE/DELETE and use storage."),
                ("Which normal form eliminates transitive dependencies?", "1NF", "2NF", "3NF", "BCNF", "c", "3NF requires that non-key columns depend only on the primary key, eliminating transitive dependencies where column A → B → C."),
                ("What does COUNT(*) return?", "Sum of all values", "Number of non-null values in a column", "Total number of rows (including NULLs)", "Average value", "c", "COUNT(*) counts all rows including those with NULL values. COUNT(column_name) counts only non-NULL values in that column."),
            ]
        }
    },
]

def seed():
    # Clear existing data
    db.query(models.LessonCompletion).delete()
    db.query(models.QuizResult).delete()
    db.query(models.UserProgress).delete()
    db.query(models.Question).delete()
    db.query(models.Quiz).delete()
    db.query(models.Lesson).delete()
    db.query(models.Course).delete()
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