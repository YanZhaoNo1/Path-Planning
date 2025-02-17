
#define BOOST_BIND_GLOBAL_PLACEHOLDERS
#include <ros/ros.h>
#include <costmap_2d/costmap_2d_ros.h>
#include <costmap_2d/costmap_2d.h>
#include <nav_core/base_global_planner.h>

#include "pathSplineSmoother/pathSplineSmoother.h"
#include<tf/transform_broadcaster.h>
#include <geometry_msgs/PoseStamped.h>
#include <nav_msgs/Path.h>

#include <fstream>

#include <vector>
#include <queue>
#define infinity 1.0e10
using namespace std;


struct Node{
  float cost;
  int index;
  //int id;
};



namespace astar_planner {
    class AstarPlanner : public nav_core::BaseGlobalPlanner{
        public:
            AstarPlanner();
            AstarPlanner(std::string name, costmap_2d::Costmap2DROS* costmap_ros);
            
       /**
       * @brief  Initialization function for the DijstraPlanner
       * @param  name The name of this planner
       * @param  costmap_ros A pointer to the ROS wrapper of the costmap to use for planning
       */
      void initialize(std::string name, costmap_2d::Costmap2DROS* costmap_ros);

      /**
       * @brief Given a goal pose in the world, compute a plan
       * @param start The start pose 
       * @param goal The goal pose 
       * @param plan The plan... filled by the planner
       * @return True if a valid plan was found, false otherwise
       */
      bool makePlan(const geometry_msgs::PoseStamped& start, 
          const geometry_msgs::PoseStamped& goal, std::vector<geometry_msgs::PoseStamped>& plan);
      
      int width;
      int height;
      int map_size;
     //vector<bool> OGM;

      double getHeuristic(int cell_index, int goal_index);
      
      vector<int> get_neighbors(int current_cell);
      double getMoveCost(int firstIndex, int secondIndex);

      bool isInBounds(int x, int y);    
      /**
      * @brief  Publish a path for visualization purposes
      */
      void publishPlan(const std::vector<geometry_msgs::PoseStamped>& path);
        
      ros::Publisher plan_pub_;
      std::string frame_id_;
	  bool initialized_=false;
	  costmap_2d::Costmap2DROS* costmap_ros_;
	  costmap_2d::Costmap2D* costmap_;

    //heuristic_function_
    std::string heuristic_name_;

    //! heuristic_factor_  启发系数
    float heuristic_factor_;
    float cost_weight;
    float ymovecost;
    float xmovecost;
    float yymovecost;
    float xxmovecost;

     //! inaccessible_cost
  float inaccessible_cost_;

  //! goal_search_tolerance
  float  goal_search_tolerance_;

    double move_cost;
    //! gridmap cost array
  unsigned char *cost_;

  vector<RealPoint> SmoothPlan(vector<int> path);
 bool smooth;
PathSplineSmoother *spline_smoother_;
int smooth_size_;
 std::string tf_prefix_;
double costnum;
    };
};
