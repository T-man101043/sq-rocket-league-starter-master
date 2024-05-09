  #This file is for strategy

from util.objects import *
from util.routines import *
from rlbot.agents.base_agent import BaseAgent 
from rlbot.utils.structures.quick_chats import QuickChats 
from util.tools import find_hits
class Bot(GoslingAgent):
     # This function runs every in-game tick (every time the game updates anything)
  # BASIC RUNNING STUFF  
    
    def run(self):
        #SETTING KICK OFF INTENT AND BASE (NONE) INTENT
        
    

        
        if self.get_intent() is not None:
            return
        
        if self.me.demolished == True:
            print('STARTING DEMO RECOVERY')
            self.set_intent(demo_recovery())
            return
        
        if self.kickoff_flag:
          #kickoff intent 
           print('KICK DA BALL!!!')
           self.set_intent(kickoff())
           return
       
        
        #HITTING STUFF
        targets = {
         'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
         'away_from_our_net' : (self.friend_goal.right_post, self.friend_goal.left_post)
      }    
        hits = find_hits(self, targets)
        if len(hits['at_opponent_goal']) > 0:
            self.set_intent(hits['at_opponent_goal'][0])
            print("I ATTACKIN")
            return
        if len(hits['away_from_our_net']) > 0:
            self.set_intent(hits['away_from_our_net'][0])
            print("I DEFINEDING")
            return
        
        #GETTING BOOST
        closest_boost = self.get_closest_boost()


        #DEFALT INTENT

        if self.get_intent() is None:
            print('BEIN A BASIC B')
            self.set_intent(goto(self.ball.location))


        #BOOST GETTING RULES
        if self.me.boost <= 5:
            if closest_boost is not None:
                print('BOOOOOOOST!!!!!!!!!')
                self.set_intent(goto(closest_boost.location))
                return
        
        print("I'm lost coach!")

        #Troll Chatting
        





 #from rlbot.agents.base_agent import BaseAgent
# from rlbot.utils.structures.quick_chats import QuickChats


# class QuickChatExampleAgent(BaseAgent):
#     def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
#         controller = SimpleControllerState()
#         self.send_quick_chat(QuickChats.CHAT_EVERYONE, QuickChats.Reactions_Wow)

#         return controller
            
          
#HIIIIIIIIIIIIIIIIIIIIIIIII THIS IS MADE TO SEE IF I Am MAKING ANY CHANGES    




