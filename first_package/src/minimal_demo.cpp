#include <rclcpp/rclcpp.hpp>

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);
    auto node = rclcpp::Node::make_shared("minimal_cpp");
    RCLCPP_ERROR_STREAM(node->get_logger(), "Hello from " << node->get_name());
    rclcpp::shutdown();
    return 0;
}