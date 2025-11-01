What I Learned from Implementing a Multi-Agent Workflow
Implementing this multi-agent workflow demonstrated how task specialization significantly improves output quality. By separating planning from validation, each agent focused on its strength—the Planner on creative itinerary design using its knowledge base, and the Reviewer on real-time fact-checking. This mirrors professional workflows where different experts handle distinct project phases.
The most valuable lesson was understanding how tool access shapes agent capabilities. The Planner works from general knowledge to create comprehensive itineraries without getting distracted by verification tasks, while the Reviewer uses internet_search to validate specific details like opening hours and prices. This asymmetry creates an efficient pipeline where creativity precedes validation.
I learned that explicit role definition in prompts is crucial. Clear instructions like "work entirely from your knowledge" for the Planner and "create a Delta List of specific changes" for the Reviewer ensured predictable, structured outputs that made the multi-agent interaction seamless.
Challenges and Solutions
The primary challenge was preventing the Reviewer from completely rewriting the Planner's work. I addressed this by explicitly instructing it to "preserve good elements while fixing problems" and provide a transparent Delta List explaining each change. This maintained efficiency while ensuring quality.
Another challenge was guaranteeing the Reviewer actually used the internet search tool. Making tool usage explicit with phrases like "Verify factual accuracy using the internet_search tool" and listing specific verification tasks solved this issue.
Balancing prompt detail proved tricky—too vague resulted in missed requirements, while overly prescriptive outputs felt rigid. I settled on clear structural requirements while allowing content flexibility.
Creative Design Choices
I emphasized geographic clustering in the Planner prompt to minimize travel time between activities, a practical consideration often overlooked. For budget-conscious travelers, I included instructions to highlight free or low-cost alternatives.
The Reviewer's Delta List format makes changes transparent and educational, showing users not just the final itinerary but why modifications were necessary. This builds trust in the system's recommendations.
I structured both prompts with labeled sections (Requirements, Tasks, Format) for clarity and maintainability, making future modifications straightforward.

External Tools and GenAI Assistance
After I follow the instruction and write out all the itinery details that the AI agent will be responding to the user's prompt, I asked Claude AI to polish my prompt and make it more clear and organize.