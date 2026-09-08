package CollectionFramework;

import java.util.ArrayList;

public class Streams {
    public static void main(String[] args) {
        ArrayList<Student> list = new ArrayList<>();

        list.add(new Student(1, "Rahul", 85));
        list.add(new Student(2, "Amit", 90));
        list.add(new Student(3, "Neha", 78));
        list.add(new Student(4, "Raj", 88));
        list.add(new Student(5, "Priya", 92));
        list.add(new Student(6, "Vikas", 75));
        list.add(new Student(7, "Anjali", 81));
        list.add(new Student(8, "Rohan", 95));
        list.add(new Student(9, "Sneha", 87));
        list.add(new Student(10, "Arjun", 80));

        list
                .stream()
                .forEach((element) -> {
                    if (element.marks.compareTo(35) < 0) {
                        System.out.println(element.name);
                    }
                });

        list.stream()
                .filter(student -> {
                    return student.marks.compareTo(35) > 0;
                })
                .map(student -> {
                    // ArrayList<String> pass = new ArrayList<>();
                    // pass.add(student.name);

                    String pass = student.name;
                    return pass;
                })
                .toList()
                .forEach(System.out::println);

    }
}

class Student {
    int id;
    String name;
    Integer marks;

    Student(int id, String name, int marks) {
        this.id = id;
        this.name = name;
        this.marks = marks;
    }
}
