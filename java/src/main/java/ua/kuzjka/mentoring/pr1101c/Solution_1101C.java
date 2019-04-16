package ua.kuzjka.mentoring.pr1101c;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Solution_1101C {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int queries = scanner.nextInt();
        for (int q = 0; q < queries; ++q) {
            int segmentNum = scanner.nextInt();
            List<Segment> segments = new ArrayList<>();
            for (int i = 0; i < segmentNum; ++i) {
                segments.add(new Segment(scanner.nextInt(), scanner.nextInt()));
            }
            boolean solved = solve(segments);
            if (solved) {
                System.out.println(segments.stream()
                        .map(s -> s.isFirstGroup() ? "1" : "2")
                        .collect(Collectors.joining(" "))
                );
            } else {
                System.out.println("-1");
            }
        }
    }

    /**
     * Tries to found solution, by finding 'gap' inside sorted segment sequence. Solution is appended as 'firstGroup'
     * flag to each segment.
     * @param segments  Input segments
     * @return          {@code true} if the solution is found, {@code false} otherwise
     */
    public static boolean solve(List<Segment> segments) {
        segments = new ArrayList<Segment>(segments);
        segments.sort(Comparator.comparing(Segment::getBegin));
        int end = segments.get(0).getEnd();
        boolean firstGroup = true;
        for (Segment s : segments) {
            if (s.getBegin() > end) {
                return true;
            } else {
                if (s.getEnd() > end) end = s.getEnd();
                s.setFirstGroup(true);
            }
        }
        return false;
    }

    static class Segment {
        private boolean firstGroup;
        private int begin;
        private int end;

        public Segment(int begin, int end) {
            this.begin = begin;
            this.end = end;
        }

        public int getBegin() {
            return begin;
        }

        public int getEnd() {
            return end;
        }

        public boolean isFirstGroup() {
            return firstGroup;
        }

        public void setFirstGroup(boolean firstGroup) {
            this.firstGroup = firstGroup;
        }
    }

    static class CannotSolveException extends RuntimeException {

    }
}
