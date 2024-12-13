from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        ''' Set voting IDs '''
        self.allowed_voter_ids = {"123456", "234567", "345678", "456789", "567890", "678901"}

        """ Voting """
        self.james_votes = 0
        self.alexis_votes = 0
        self.voters = set()  # To track IDs of voters who voted

        # Connect button to functionality
        self.submit_button.clicked.connect(lambda: self.submit_vote())

    def submit_vote(self):
        voter_id = self.id_box.toPlainText().strip()  # Access id_box directly
        if not voter_id:
            self.status_label.setText("Please enter your ID number")
            return

        # Validate voter ID
        if voter_id not in self.allowed_voter_ids:
            self.status_label.setText("Invalid ID!")
            return
        if voter_id in self.voters:
            self.status_label.setText("Already voted!")
            return

        # Check if a candidate is selected
        if self.first_button.isChecked():
            self.james_votes += 1
        elif self.second_button.isChecked():
            self.alexis_votes += 1
        else:
            self.status_label.setText("No candidate selected")
            return

        # Record the voter ID and show success message
        self.voters.add(voter_id)
        self.status_label.setText("Thank you for voting!")

        # Clear the ID box and radio buttons
        self.id_box.clear()
        self.first_button.setAutoExclusive(False)
        self.second_button.setAutoExclusive(False)
        self.first_button.setChecked(False)
        self.second_button.setChecked(False)
        self.first_button.setAutoExclusive(True)
        self.second_button.setAutoExclusive(True)

        # End voting after all voters
        if len(self.voters) == len(self.allowed_voter_ids):
            self.end_voting()

    def end_voting(self):
        if self.james_votes > self.alexis_votes:
            winner = "James"

        elif self.alexis_votes > self.james_votes:
            winner = "Alexis"
        else:
            winner = "It's a tie!"

        result_message = f"The Winner is: {winner}\n\nResults:\nJames: {self.james_votes} votes\nAlexis: {self.alexis_votes} votes"
        self.status_label.setText(result_message)
        self.submit_button.setDisabled(True)



#https://www.freecodecamp.org/news/python-lambda-function-explained/
#https://www.youtube.com/watch?v=KqyZc6uR9QU

