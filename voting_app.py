class VotingApp:
    def __init__(self):
        self.candidates = {}

    def add_candidate(self, candidate_name):
        self.candidates[candidate_name] = 0

    def vote(self, candidate_name):
        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
            print(f"Voted for {candidate_name}")
        else:
            print("Invalid candidate")

    def show_results(self):
        print("Voting Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")

def main():
    voting_app = VotingApp()

    while True:
        print("1. Add Candidate")
        print("2. Vote")
        print("3. Show Results")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            candidate_name = input("Enter candidate name: ")
            voting_app.add_candidate(candidate_name)
        elif choice == "2":
            candidate_name = input("Enter candidate name: ")
            voting_app.vote(candidate_name)
        elif choice == "3":
            voting_app.show_results()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

