import pygame
import sys

from const import *
from game import Game
from move import Move
from square import Square

class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show funcs
            screen.fill('black', ((0, 0), (WIDTH, HEIGHT)))
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_hover(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    
                    if Square.in_range(clicked_col, clicked_row):
                        # if clicked square has a piece
                        if board.squares[clicked_row][clicked_col].has_piece():
                            piece = board.squares[clicked_row][clicked_col].piece

                            # valid piece (color) ?
                            if piece.color == game.next_player:
                                board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                                dragger.save_initial(event.pos)
                                dragger.drag_piece(piece)

                                # show funcs
                                game.show_bg(screen)
                                game.show_last_move(screen)
                                game.show_moves(screen)
                                game.show_hover(screen)
                                game.show_pieces(screen)

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    
                    if Square.in_range(motion_row, motion_col):
                        game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show funcs
                        screen.fill('black', ((0, 0), (WIDTH, HEIGHT)))
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_hover(screen)
                        game.show_pieces(screen)

                        dragger.update_blit(screen)
                        
    
                # end click
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(dragger.piece, move):
                            #capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)

                            board.set_true_en_passant(dragger.piece)
                            
                            # sound
                            game.sound_effect(captured)
                            # next turn
                            game.next_turn()

                        dragger.undrag_piece()


                elif event.type == pygame.KEYDOWN:
                    
                    # change theme 
                    if event.key == pygame.K_t:
                        game.change_theme()

                    # reset game
                    if event.key == pygame.K_r:
                        game.reset_game()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger


                # close app
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            pygame.display.update()


main = Main()
main.mainloop()