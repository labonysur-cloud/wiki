import pandas as pd
import numpy as np
from core.memory import Memory
from core import tools  # Import tools functions

class Brain:
    def __init__(self, dataset_paths):
        """
        Initialize the Wiki Brain.
        dataset_paths: list of CSV paths containing commands/responses
        """
        # Load all datasets and merge
        self.brain_df = pd.concat([pd.read_csv(path) for path in dataset_paths], ignore_index=True)
        
        # Ensure required columns
        if 'command' not in self.brain_df.columns or 'response' not in self.brain_df.columns:
            raise ValueError("Each dataset must have 'command' and 'response' columns.")
        
        # Optional: 'category' column
        if 'category' not in self.brain_df.columns:
            self.brain_df['category'] = None
        
        # Load memory
        self.memory = Memory()

    def similarity(self, a, b):
        """Simple keyword-overlap similarity"""
        a_set = set(a.lower().split())
        b_set = set(b.lower().split())
        return len(a_set & b_set) / max(len(a_set), 1)

    def find_best_match(self, input_text):
        """Return the best matching command and its response"""
        commands = self.brain_df['command'].values
        responses = self.brain_df['response'].values
        categories = self.brain_df['category'].values
        
        sims = np.array([self.similarity(input_text, cmd) for cmd in commands])
        idx = np.argmax(sims)
        
        if sims[idx] < 0.1:
            return None, "Sorry Babe , I didn't understand that.", None
        else:
            return commands[idx], responses[idx], categories[idx]

    def respond(self, input_text):
        """Generate response for user input"""
        input_text = input_text.lower()
        
        command, response, category = self.find_best_match(input_text)
        
        # ======== Handle Tools ========
        if category == "tools":
            if "timer" in input_text:
                # Example: "set timer for 5 minutes" → extract number
                import re
                nums = re.findall(r'\d+', input_text)
                seconds = int(nums[0])*60 if nums else 60
                response = tools.start_timer("default", seconds)
            elif "open" in input_text:
                if "." in input_text or "website" in input_text:
                    # open website
                    site = input_text.split("open")[-1].strip()
                    response = tools.open_website(site)
                else:
                    # open app
                    app = input_text.split("open")[-1].strip()
                    response = tools.open_app(app)
        
        # Save to memory
        self.memory.save(input_text, response)
        return response

    def add_command(self, command, response, category=None):
        """Add a new command dynamically"""
        new_row = {'command': command, 'response': response, 'category': category}
        self.brain_df = pd.concat([self.brain_df, pd.DataFrame([new_row])], ignore_index=True)