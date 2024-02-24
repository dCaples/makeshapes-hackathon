import time
import os

from openai import OpenAI

openai_key = "INSERT YOUR OPENAI KEY HERE"
if openai_key == "INSERT YOUR OPENAI KEY HERE":
    raise ValueError("Please insert your OpenAI key in the ai.py file. You can get a key from OpenAI's website.")

client = OpenAI(api_key=openai_key)


background_information = "Dogs are the best pets. They are loyal and friendly. They are also very cute."

background_information = """
Unconscious Bias 


Course: Understanding and Addressing Unconscious Bias


Course Description:
Understanding and Addressing Unconscious Bias is a comprehensive learning experience designed to help participants recognize, understand, and mitigate the impact of unconscious bias in the workplace. Through a series of engaging activities and discussions, participants will explore the origins and manifestations of bias, learn practical strategies for challenging bias in decision-making processes, and develop skills for fostering a more inclusive and equitable work environment.


Learning Outcomes:
By the end of this course, participants will be able to:


Recognize and acknowledge their own unconscious biases.
Understand how unconscious bias influences individual and organizational behavior.
Identify strategies for challenging unconscious bias in decision-making processes.
Foster a more inclusive and equitable workplace culture.
Course Outline:


Introduction to Unconscious Bias


Overview of unconscious bias and its impact on workplace dynamics.
Video: Exploring the concept of unconscious bias.
Group Discussion: Sharing personal experiences and perspectives on bias.
Understanding Bias in Decision Making


Discussion: Examining how bias influences decision-making processes.
Poll: Identifying common biases and their effects on organizational outcomes.
Group Activity: Analyzing case studies to understand the implications of bias in real-world scenarios.
Strategies for Challenging Unconscious Bias


Video: Introducing practical strategies for challenging unconscious bias.
Drawing Activity: Visualizing alternative perspectives and viewpoints.
Word Cloud: Sharing strategies for promoting inclusivity and equity in the workplace.
Creating an Inclusive Work Environment


Discussion: Exploring the role of leadership in addressing unconscious bias.
Post-it Activity: Brainstorming actionable steps for creating a more inclusive workplace culture.
Reflection: Reflecting on personal commitments to fostering diversity and equity.
Summary of Course:
Understanding and Addressing Unconscious Bias is a transformative learning experience that equips participants with the knowledge, skills, and strategies needed to recognize and mitigate the impact of bias in the workplace. Through engaging activities, discussions, and practical exercises, participants will gain a deeper understanding of unconscious bias, explore its implications for decision-making processes, and learn how to foster a more inclusive and equitable work environment where all employees feel valued and respected.


FAQ: Understanding and Addressing Unconscious Bias


What is unconscious bias?


Unconscious bias refers to the automatic, ingrained stereotypes and attitudes that influence our understanding, actions, and decisions without our conscious awareness.
How does unconscious bias manifest in the workplace?


Unconscious bias can manifest in various ways in the workplace, including during hiring and promotion decisions, performance evaluations, team dynamics, and interactions with colleagues and clients.
Why is it important to address unconscious bias?


Addressing unconscious bias is crucial for creating a more inclusive and equitable workplace culture. By acknowledging and mitigating bias, organizations can foster diversity, enhance team collaboration, improve decision-making processes, and promote fairness and equality for all employees.
How can I recognize my own unconscious biases?


Recognizing unconscious biases requires self-awareness and introspection. Engaging in activities such as reflection, feedback solicitation from others, and participating in bias awareness training can help individuals identify their own biases and understand how they influence their thoughts and actions.
What are some strategies for challenging unconscious bias?


Strategies for challenging unconscious bias include cultivating empathy and perspective-taking, consciously questioning assumptions and stereotypes, seeking out diverse perspectives and experiences, practicing mindfulness and reflection, and fostering inclusive environments where all voices are heard and valued.
How can I address unconscious bias in decision-making processes?


To address unconscious bias in decision-making processes, organizations can implement strategies such as blind resume screening, structured interview processes, diverse hiring panels, bias-awareness training for employees, and regular reviews of policies and practices to identify and mitigate bias.
What role does leadership play in addressing unconscious bias?


Leadership plays a critical role in driving organizational change and promoting inclusivity. Leaders can lead by example, prioritize diversity and equity initiatives, allocate resources for bias training and education, hold themselves and others accountable for addressing bias, and create a culture of openness, transparency, and continuous improvement.
How can I support colleagues who experience bias or discrimination?


Supporting colleagues who experience bias or discrimination involves listening empathetically, validating their experiences, offering support and resources, advocating for their needs, and actively working to create a safe and inclusive environment where all employees feel valued and respected.
What are some common misconceptions about unconscious bias?


Common misconceptions about unconscious bias include the belief that bias only affects certain individuals or groups, that it can be easily overcome through sheer willpower, or that it is not as prevalent in today's society. Recognizing and addressing these misconceptions is essential for fostering meaningful change.
How can organizations measure progress in addressing unconscious bias?


Organizations can measure progress in addressing unconscious bias through various methods, including conducting employee surveys to assess perceptions of inclusivity and fairness, tracking diversity metrics such as representation and retention rates, analyzing outcomes of diversity and inclusion initiatives, and seeking feedback from employees on the effectiveness of bias-awareness training and other interventions. Regular monitoring and evaluation are essential for identifying areas of improvement and sustaining progress over time.
"""


def generate_question_answer(question):
    # wait for 5 seconds to simulate a long running task
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": "Answer questions. Respond in plain text, NO MARKDOWN!"
        },
        {
          "role": "user",
          "content": f"Here some background infomration is: {background_information}"
        },
        {
            "role": "user",
            "content": f"{question}"
        }
      ],
      temperature=1,
      max_tokens=1088,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content