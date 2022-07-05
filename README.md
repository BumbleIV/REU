&nbsp;
<img align="left" alt="git" width="24px" src="https://user-images.githubusercontent.com/67522964/147704862-04267bff-13d7-439f-821d-97ab785a8792.png" /> 
<img align="left" alt="git" width="24px" src="https://user-images.githubusercontent.com/67522964/147705253-d3f9d43f-0559-4d4e-b55b-0ab5f287bacd.png" /> 
<img align="left" alt="git" width="24px" src="https://user-images.githubusercontent.com/67522964/147704862-04267bff-13d7-439f-821d-97ab785a8792.png" /> 
<img align="left" alt="git" width="24px" src="https://user-images.githubusercontent.com/67522964/147705253-d3f9d43f-0559-4d4e-b55b-0ab5f287bacd.png" /> 
<img align="left" alt="git" width="24px" src="https://user-images.githubusercontent.com/67522964/147704862-04267bff-13d7-439f-821d-97ab785a8792.png" />  

### Information Sciences Institute <img align="right" alt="git" width="24px" src="https://user-images.githubusercontent.com/67522964/147623227-9dbfbed3-bd34-46d7-9a02-ca11fff50add.png" />

___
**About:** 
&nbsp;

Repository containing code I developed during my time as a Software Engineer Intern for USC's Information Science Institute. 

I conduct research alongside Professor [Mayank Kejriwal](https://usc-isi-i2.github.io/kejriwal/) on his work regarding [Open-World Game Theory](https://reu.isi.edu/projects.html). We study AI systems applied to real-world settings with multiple selfishly-maximizing agents by utilizing Game Theory to model informational complexity of various environments, agent payoffs, decision matrices, and incomplete information. This internship is through the National Science Foundation (NSF)’s [Research Experience for Undergraduates (REU)](https://www.nsf.gov/crssprgm/reu/) program. 


**Technologies:**
&nbsp;

<img align="left" alt="python" width="32px" src="https://unpkg.com/simple-icons@v6/icons/python.svg" /> 


**Brownian Motion Simulation:**
# Input
# Network Model: G = (V, E)
# V = set of vertices (nodes)
# E = set of edges
# Number of Iterations: n
# Number of Blue Balls per node: blue (5 balls for now)
# Number of Red Balls per node: red (5 balls for now)

# Output:
&nbsp;
# M = {ball_ID: [node_ID, node_ID, ...], ball_ID: [node_ID, node_ID, ...], ...}

# Algorithm:
# 1. Initialize M = {}
# 2. Attribute each node in G a blue_amt and red_amt balls
# 3. Enter blue_IDs and red_IDs into M as keys with empty lists as values
# 4. Copy G into V_2 then randomize (and fix) the order of nodes in V_2
# 5. Select current_node and neighbor_node from V_2
# 6. Randomly sample 1 ball each from current_node and neighbor_node then apply following rules:
#    a. If both balls sampled are the same color, the no transaction occurs
#    b. If both balls sampled are different colors, the red ball is removed from its owner node and given to the opposing node
#       b1. Append the node_ID of V_2 that the red ball is moved to into the list of values of the key of the ball_ID
# 7. Repeat steps 6 until all neighbor_node of current_node are visited
# 8. Select next current_node in V_2
# 9. Repeat steps 6-8 until n iterations are completed
# 10. Return M

&nbsp;
