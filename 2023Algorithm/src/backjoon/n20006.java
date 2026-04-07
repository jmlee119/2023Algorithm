package backjoon;
import java.util.*;
import java.io.*;

public class n20006 {
    static class Player {
        int level;
        String name;
        Player(int level, String name) {
            this.level = level;
            this.name = name;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int P = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Player[] player = new Player[P];
        for (int i = 0; i < P; i++) {
            st = new StringTokenizer(br.readLine());
            int level = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            player[i] = new Player(level, name);
        }
        List<List<Player>> room = new ArrayList<>();
        List<Integer> playerLevel = new ArrayList<>();

        for (int i = 0; i < P; i++) {
            Player current = player[i];
            boolean enter = false;
            for (int j = 0; j < room.size(); j++) {
                int room_num = playerLevel.get(j);

                if (room.get(j).size() < M && room_num - 10 <= current.level && current.level <= room_num + 10) {
                    room.get(j).add(current);
                    enter = true;
                    break;
                }
            }
            if (!enter) {
                playerLevel.add(current.level);
                List<Player> new_Room = new ArrayList<>();
                new_Room.add(current);
                room.add(new_Room);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < room.size(); i++) {
            List<Player> ro = room.get(i);
            if (ro.size() == M) {
                sb.append("Started!\n");
            } else {
                sb.append("Waiting!\n");
            }
            ro.sort((a, b) -> a.name.compareTo(b.name));
            for (int j = 0; j < ro.size(); j++) {
                sb.append(ro.get(j).level).append(" ").append(ro.get(j).name).append("\n");
            }
        }
        System.out.println(sb);
    }
}
