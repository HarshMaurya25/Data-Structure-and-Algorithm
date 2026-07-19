import java.util.ArrayList;
import java.util.List;

public class Partition {
    public static void main(String[] args) {

        String s = "abaca";
        List<List<String>> Answer = new ArrayList<>();
        Partitions(s, new ArrayList<>(), Answer);

        System.out.println(Answer.toString());

    }

    public static void Partitions(String s, List<String> Partition, List<List<String>> Answer) {

        if (s.length() == 0) {
            Answer.add(new ArrayList<>(Partition));
            return;
        }

        for (int i = 0; i < s.length(); i++) {
            String part = s.substring(0, i + 1);

            Partition.add(part);
            Partitions(s.substring(i + 1), Partition, Answer);
            Partition.remove(part);
        }

    }

    public static List<List<String>> partitions(String s, List<String> partition) {

        List<List<String>> answer = new ArrayList<>();

        // Base case
        if (s.length() == 0) {
            answer.add(new ArrayList<>(partition));
            return answer;
        }

        for (int i = 0; i < s.length(); i++) {

            String part = s.substring(0, i + 1);

            partition.add(part);

            answer.addAll(partitions(s.substring(i + 1), partition));

            partition.remove(partition.size() - 1);
        }

        return answer;
    }
}