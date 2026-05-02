class Solution {
private:
    std::unordered_map<int, std::vector<int>> indices;

public:
    Solution(std::vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            indices[nums[i]].push_back(i);
        }
    }

    int pick(int target) {
        std::random_device rd;
        std::mt19937 gen(rd());

        if (indices.find(target) != indices.end()) {
            std::vector<int>& targetIndices = indices[target];
            std::uniform_int_distribution<int> dist(0, targetIndices.size() - 1);
            int randomIndex = dist(gen);
            return targetIndices[randomIndex];
        }

        return -1;
    }
};