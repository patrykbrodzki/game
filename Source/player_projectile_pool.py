from Source.queue import Queue
from Source.projectile_object import Projectile


class ProjectilePool:
    # for different projectiles it is possible to have different/split pools
    projectile_pool = None

    def __init__(self, capacity, screen):
        self.capacity = capacity
        self.projectile_pool = Queue(self.capacity)
        self.screen = screen

    def __repr__(self):
        return self.projectile_pool.display_all_elements()

    def __len__(self):
        return self.projectile_pool.queue_size()

    def initiate(self):
        for i in range(self.capacity):
            self.projectile_pool.add_to_queue(Projectile(self.screen, 20))

    def show_all(self):
        return self.projectile_pool.display_all_elements()

    def get_object(self):
        return self.projectile_pool.get_from_queue()

    def return_object(self, object_to_return):
        self.projectile_pool.add_to_queue(object_to_return)

    # BELOW methods with loops for fire and animate could be replaced with linked list queue
    def fire(self, movement_direction, player_position):
        # Check status of projectile. If it is non active take that projectile and change status to active.
        for projectile_to_fire in self.projectile_pool.queue:
            if projectile_to_fire.active:
                continue
            else:
                projectile_to_fire = self.get_object()
                # set active sets projectile as active and sets x and y position for the projectile to start from
                projectile_to_fire.activate(movement_direction, player_position)
                self.return_object(projectile_to_fire)

    def animate(self):
        # Animate projectile when its status is active
        for projectile in self.projectile_pool.queue:
            if projectile.active:
                # print values for debugging purposes (check if objects in memory are the same)
                # print('Active -->  ', projectile)
                projectile.draw()
            # else:
            #     print('NOT ACTIVE -->  ', projectile)