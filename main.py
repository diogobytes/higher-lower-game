
import art
import game_data
import random 
import os

total_points =  0
continue_playing = True


while continue_playing:
  generate_index_1 = random.randint(0, len(game_data.data) - 1)
  generate_index_2 = random.randint(0, len(game_data.data) - 1)
  print(art.logo)
  print(f"You're right! current score: {total_points} ")
  print(f"Compare A: {game_data.data[generate_index_1]['name']}, a {game_data.data[generate_index_1]['description']}, from {game_data.data[generate_index_1]['country']} ")

  print(art.vs)
  print(f"Compare B: {game_data.data[generate_index_2]['name']}, a {game_data.data[generate_index_2]['description']}, from {game_data.data[generate_index_2]['country']} ")

  guess = input("Who has more followers? Type 'A' or 'B' ")
  follower_count_A = game_data.data[generate_index_2]['follower_count']
  follower_count_B = game_data.data[generate_index_1]['follower_count']
  if follower_count_A > follower_count_B and guess == 'A':
    total_points += 1
    os.system('clear')
  if follower_count_A > follower_count_B and guess == 'B':
    continue_playing = False
    print("You lose!")
    break
  if follower_count_B > follower_count_A and guess == 'B':
    total_points += 1
    os.system('clear')
  if follower_count_B > follower_count_A and guess == 'A':
    continue_playing = False
    print("You lose!")
    break