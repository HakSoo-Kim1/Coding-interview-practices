import java.util.*;

public class BestAlbum {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < genres.length; i++) {
            if (hashMap.get(genres[i]) == null)
                hashMap.put(genres[i], plays[i]);
            else
                hashMap.put(genres[i], plays[i] + hashMap.get(genres[i]));
        }
        Map<String, Integer> sortedMap = new TreeMap<>(new Comparator<String>() {
            public int compare(String o1, String o2) {
                return 1;
            }
        });
        sortedMap.putAll(hashMap);
        ArrayList<Integer> answerArrayList = new ArrayList<>();
        for (Map.Entry<String, Integer> genre : hashMap.entrySet()) {
            TreeMap<Integer, Integer> genreMap = new TreeMap<>(Collections.reverseOrder());
            for (int i = 0; i < plays.length; i++) {
                if (genres[i] == genre.getKey()) {
                    genreMap.put(plays[i], i);
                    System.out.println(genreMap);
                }
            }
            System.out.println(genreMap);
            List<Integer> indexes = new ArrayList<Integer>(genreMap.values());
            for (int i = 0; i < 2 && i < indexes.size(); i++)
                answerArrayList.add(indexes.get(i));
        }
        System.out.println(answerArrayList);
        int[] arr = answerArrayList.stream().mapToInt(i -> i).toArray();

        return arr;
    }


        public static void main (String[] args){
            String [] genres = {"classic", "pop", "classic", "classic", "pop"};
            int [] plays = {500,600,150,800,2500};
            BestAlbum c = new BestAlbum();
        int[] a = c.solution(genres,plays);
        for (int each : a)
        System.out.println (each);

        }
    }


