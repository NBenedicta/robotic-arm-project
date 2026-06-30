from geometry_msgs.msg import Pose
from moveit_msgs.msg import CollisionObject
from shape_msgs.msg import SolidPrimitive


class SceneManager:
    def __init__(self, node):
        self.publisher = node.create_publisher(CollisionObject, "/collision_object", 10)

    def add_box(self):
        box = CollisionObject()
        box.header.frame_id = "panda_link0"
        box.id = "obstacle_box"

        primitive = SolidPrimitive()
        primitive.type = SolidPrimitive.BOX
        primitive.dimensions = [0.20, 0.20, 0.20]

        pose = Pose()
        pose.position.x = 0.45
        pose.position.y = 0.0
        pose.position.z = 0.25
        pose.orientation.w = 1.0

        box.primitives.append(primitive)
        box.primitive_poses.append(pose)
        box.operation = CollisionObject.ADD

        self.publisher.publish(box)
        print("Obstacle box added to planning scene.")