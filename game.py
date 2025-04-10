import tkinter as tk
import time
from node import Node, player_make_move, ai_make_move, get_winner
from algorithms import min_max, alpha_beta, visited_nodes_count

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skaitļu Secības Spēle")
        self.root.state("zoomed")

        # Atļauj mainīt loga izmēru
        self.root.resizable(True, True)
        self.init_main_menu()
    

    def init_main_menu(self):
        self.clear_window()
        play_button = tk.Button(self.root, text="Spēlēt", font=("Arial", 28), command=self.choose_ai_algorithm, bg="#ccdcf7")
        play_button.pack(expand=True, ipadx=65, ipady=35)
    

    def choose_ai_algorithm(self):
        self.clear_window()
        
        container = tk.Frame(self.root)
        container.pack(expand=True, fill=tk.BOTH)

        label = tk.Label(container, text="Kādu algoritmu izmantos dators?", font=("Arial", 24))
        label.pack(pady=(150, 0))

        frame = tk.Frame(container)
        frame.pack(expand=True)

        min_max_button = tk.Button(frame, text="Min-Max", font=("Arial", 16), command=lambda: self.choose_first_player("min-max"), bg="#ccdcf7")
        min_max_button.pack(side=tk.LEFT, padx=20, ipadx=65, ipady=35)

        alpha_beta_button = tk.Button(frame, text="Alpha-Beta", font=("Arial", 16), command=lambda: self.choose_first_player("alpha-beta"), bg="#ccdcf7")
        alpha_beta_button.pack(side=tk.RIGHT, padx=20, ipadx=65, ipady=35)


    def choose_first_player(self, algorithm):
        self.algorithm = algorithm

        self.clear_window()
        
        container = tk.Frame(self.root)
        container.pack(expand=True, fill=tk.BOTH)

        label = tk.Label(container, text="Kurš sāk pirmais?", font=("Arial", 24))
        label.pack(pady=(150, 0))

        frame = tk.Frame(container)
        frame.pack(expand=True)

        player_button = tk.Button(frame, text="Spēlētājs", font=("Arial", 16), command=lambda: self.choose_sequence_length("player"), bg="#ccdcf7")
        player_button.pack(side=tk.LEFT, padx=20, ipadx=65, ipady=35)

        ai_button = tk.Button(frame, text="Dators", font=("Arial", 16), command=lambda: self.choose_sequence_length("ai"), bg="#ccdcf7")
        ai_button.pack(side=tk.RIGHT, padx=20, ipadx=65, ipady=35)

    
    def choose_sequence_length(self, first_player):
        self.clear_window()
        label = tk.Label(self.root, text="Izvēlies secības garumu", font=("Arial", 24))
        label.pack(pady=(150, 0))
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True)
        
        for length in range(15, 26):
            button = tk.Button(button_frame, text=str(length), font=("Arial", 14), command=lambda l=length: self.start_game(l, first_player), bg="#ccdcf7")
            button.pack(side=tk.LEFT, padx=8, pady=8, ipadx=12, ipady=12)
    

    def start_game(self, length, first_player):
        self.node = Node(length=length)
        self.first_player = first_player
        self.current_player = 1 if first_player == "player" else 2
        self.update_game_ui()
    

    def update_game_ui(self):
        self.clear_window()
        
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X, pady=10)
        
        player_label = tk.Label(top_frame, text=f"Spēlētāja punkti: {self.node.first_player_points if self.first_player == 'player' else self.node.second_player_points} p.", font=("Arial", 18))
        player_label.pack(side=tk.LEFT, padx=20)
        
        ai_label = tk.Label(top_frame, text=f"Datora punkti: {self.node.second_player_points if self.first_player == 'player' else self.node.first_player_points} p.", font=("Arial", 18))
        ai_label.pack(side=tk.RIGHT, padx=20)
        
        turn_label = tk.Label(self.root, text=f"{'Spēlētāja' if self.current_player == 1 else 'Datora'} gājiens", font=("Arial", 20))
        turn_label.pack(pady=20)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True)
        
        self.buttons = []
        for index, num in enumerate(self.node.sequence):
            btn = tk.Button(button_frame, text=str(num), font=("Arial", 15), command=lambda i=index: self.make_move(i), bg="#ccdcf7")
            btn.grid(row=0, column=index, padx=5, pady=5, ipadx=8, ipady=8)
            self.buttons.append(btn)
        
        if self.current_player == 2:
            for btn in self.buttons:
                btn.config(state="disabled", bg="#ccdcf7")
            self.root.after(1000, self.ai_turn)
    

    def make_move(self, index):
        if self.current_player == 1:
            self.node = player_make_move(self.node, index)
        
        if not self.node.sequence:
            self.end_game()
            return
        
        self.current_player = 2
        self.update_game_ui()
    
    
    def ai_turn(self):
        global visited_nodes_count
        visited_nodes_count = 0
         
        if self.current_player == 2 and self.node.sequence:
            start_time = time.time()

            if self.algorithm == 'min-max':
                move = min_max(self.node)
            else:
                move = alpha_beta(self.node)
            self.node, ai_index = ai_make_move(self.node, move)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"MI gājiena laiks: {elapsed_time:.4f} sekundes")

            if 0 <= ai_index < len(self.buttons):
                self.buttons[ai_index].config(bg="red")  # Simulē pogas nospiešanu
                self.root.after(1000, lambda: self.finish_ai_move(ai_index))

    
    def finish_ai_move(self, ai_index):
        if 0 <= ai_index < len(self.buttons):
            self.buttons[ai_index].config(bg="#ccdcf7")  # Atiestata pogas krāsu

        if not self.node.sequence:
            self.end_game()
            return

        self.current_player = 1
        self.update_game_ui()

    
    def end_game(self):
        self.clear_window()

        container = tk.Frame(self.root)
        container.pack(expand=True, fill=tk.BOTH)

        winner = get_winner(self.node)
        if winner == 0:
            msg = "Neizšķirts!"
        else:
            if self.first_player == "player":
                msg = f"{'Spēlētājs' if winner == 1 else 'Dators'} uzvarēja!"
                points = f"Spēlētāja punkti: {self.node.first_player_points} \nDatora punkti: {self.node.second_player_points}"
            else:
                msg = f"{'Dators' if winner == 1 else 'Spēlētājs'} uzvarēja!"
                points = f"Spēlētāja punkti: {self.node.second_player_points} \nDatora punkti: {self.node.first_player_points}"
        
        label = tk.Label(container, text=msg, font=("Arial", 26))
        label.pack(pady=(150, 0))
        label2 = tk.Label(container, text=points, font=("Arial", 20))
        label2.pack(pady=(50, 0))

        button_frame = tk.Frame(container)
        button_frame.pack(expand=True)

        replay_button = tk.Button(button_frame, text="Spēlēt vēlreiz", font=("Arial", 15), command=self.choose_ai_algorithm, bg="#ccdcf7")
        replay_button.pack(side=tk.LEFT, padx=20, ipadx=60, ipady=30)

        exit_button = tk.Button(button_frame, text="Iziet", font=("Arial", 15), command=self.root.quit, bg="#ccdcf7")
        exit_button.pack(side=tk.RIGHT, padx=20, ipadx=60, ipady=30)

    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
