class largestAltitude {

    // First Attempt...
    // Simple Iteration Checker.
    // RT - 100.00%, MEM - 6.89%
    public int largestAltitudeFirst(int[] gain) {
        if (gain.length == 0) return 0;
        if (gain.length == 1) return Math.max(0, gain[0]);
        int best = 0;
        int cur = 0;

        for (int i = 0; i < gain.length; i++) {
            cur+=gain[i];
            if (cur > best) {
                best = cur;
            }
        }

        return best;
    }

    // Solution on Leet Code, Same Approach, Just No If Statements.
    // RT - 100.00%, MEM - 65.96%
    public int largestAltitudeMemOptimized(int[] gain) {
        int highestAltitude = 0;
        int altitude = 0;

        for (int i = 0; i < gain.length; i++) {
            altitude += gain[i]; 

            if (altitude > highestAltitude)
                highestAltitude = altitude;
        }

        return highestAltitude;
    }
}
