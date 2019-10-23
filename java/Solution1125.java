import java.util.HashSet;
import java.util.Set;

class  Solution1125 {
    public int[] smallestSufficientTeam(String[] req_skills, List<List<String>> people) {
        Set<Integer> curPeopleSet = new HashSet<>();
        Set<String> currentSkillsSet = new HashSet<>();
        Set<Integer> newSet = getSmallestTeam(req_skills, people, curPeopleSet, currentSkillsSet);

        // Set to array
        int[] arr = new int[newSet.size()];
        int i = 0;
        for (int a : newSet) {
            arr[i++] = a;
        }
        return arr;
    }

    private Set<Integer> getSmallestTeam(String[] req_skills, List<List<String>> people, Set<Integer> curPeopleSet,
            Set<String> currentSkillsSet) {
        Set<Integer> result = new HashSet<>();
        int min_length = Integer.MAX_VALUE;

        // add new people to the team
        for (int i = 0; i < people.size(); ++i) {
            if (!curPeopleSet.contains(i)) {
                Set<String> tempSkill = new HashSet<>();
                tempSkill.addAll(currentSkillsSet);
                if (testIfSufficient(req_skills, tempSkill, people.get(i))) {
                    curPeopleSet.add(i);
                    currentSkillsSet.addAll(new HashSet<>(people.get(i)));
                    System.out.println("Got it");
                    System.out.println(curPeopleSet);
                    System.out.println(currentSkillsSet);
                    return curPeopleSet;
                }
                Set<Integer> temp = new HashSet<>();
                temp.addAll(curPeopleSet);
                temp.add(i);

                Set<String> temp_skills = new HashSet<>();
                temp_skills.addAll(currentSkillsSet);
                temp_skills.addAll(new HashSet<>(people.get(i)));

                Set<Integer> newSet = getSmallestTeam(req_skills, people, temp, temp_skills);
                if (newSet.size() <= min_length) {
                    min_length = newSet.size();
                    result = newSet;
                }
            }
        }
        Set<Integer> full = new HashSet<>();
        for (int i = 0; i < people.size(); ++i)
            full.add(i);
        Set<Integer> raw = new HashSet<>();
        return (result == raw) ? full : result;
    }

    private boolean testIfSufficient(String[] req_skills, Set<String> currentSkills, List<String> newSkills) {
        currentSkills.addAll(new HashSet(newSkills));
        return req_skills.length == currentSkills.size();
    } 
}