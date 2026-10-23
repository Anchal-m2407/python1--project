 # Save this as "generate_srs_pdf.py" and run it
# Install required library first: pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def create_srs_pdf():
    doc = SimpleDocTemplate(
        "Household_Grid_Optimization_SRS.pdf",
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=16,
        alignment=TA_CENTER,
        spaceAfter=30,
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#1a5490'),
        spaceAfter=12,
        spaceBefore=12,
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=8,
        spaceBefore=8,
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )
    
    story = []
    
    # Title Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("HOUSEHOLD GRID OPTIMIZATION USING", title_style))
    story.append(Paragraph("REINFORCEMENT LEARNING", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("A Project Submitted In Partial Fulfilment of the Requirements", normal_style))
    story.append(Paragraph("For the Degree of", normal_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("BACHELOR OF TECHNOLOGY", heading1_style))
    story.append(Paragraph("In", normal_style))
    story.append(Paragraph("INFORMATION TECHNOLOGY", heading1_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("By", normal_style))
    story.append(Paragraph("Purnima Pandey: 2414670010016", normal_style))
    story.append(Paragraph("Anchal Maurya: 2414670010006", normal_style))
    story.append(Paragraph("Anju: 241467001000X", normal_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Under the Supervision of", normal_style))
    story.append(Paragraph("Dr. Suryabhan Pratap Singh", normal_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Institute of Engineering and Technology", normal_style))
    story.append(Paragraph("Deen Dayal Upadhyaya Gorakhpur University, Gorakhpur", normal_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("MARCH, 2026", normal_style))
    
    story.append(PageBreak())
    
    # Table of Contents placeholder
    story.append(Paragraph("TABLE OF CONTENTS", heading1_style))
    toc_data = [
        ["1.", "Introduction", "3"],
        ["2.", "Overall Description", "5"],
        ["3.", "System Architecture", "8"],
        ["4.", "Data Flow Diagrams", "10"],
        ["5.", "System Features", "11"],
        ["6.", "Functional Requirements", "14"],
        ["7.", "External Interface Requirements", "15"],
        ["8.", "Security and Compliance", "17"],
        ["9.", "Non-Functional Requirements", "18"],
        ["10.", "System Diagrams", "20"],
        ["11.", "Conclusion", "22"],
        ["12.", "Future Enhancements", "22"],
    ]
    toc_table = Table(toc_data, colWidths=[0.5*inch, 4*inch, 0.8*inch])
    toc_table.setStyle(TableStyle([('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
                                   ('FONTSIZE', (0,0), (-1,-1), 10),
                                   ('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
    story.append(toc_table)
    
    story.append(PageBreak())
    
    # Section 1
    story.append(Paragraph("1. INTRODUCTION", heading1_style))
    story.append(Paragraph("1.1 Purpose", heading2_style))
    story.append(Paragraph("The main purpose of this project is to develop an intelligent system that optimizes household electricity consumption using Reinforcement Learning (RL). Traditional energy management systems rely on fixed rules that cannot adapt to changing environmental conditions, leading to inefficient energy use and higher costs. This project aims to create an RL-based agent that learns optimal energy management strategies by interacting with its environment, which includes factors like electricity demand, temperature, and weather conditions.", normal_style))
    
    story.append(Paragraph("1.2 Scope of the Project", heading2_style))
    story.append(Paragraph("The scope of this project focuses on developing a simulation-based optimization model for a single household grid. The system will use Reinforcement Learning to manage electricity flow by considering real-time inputs.", normal_style))
    
    story.append(Paragraph("1.3 Definitions, Acronyms and Abbreviations", heading2_style))
    defs_data = [
        ["RL", "Reinforcement Learning"],
        ["Q-Learning", "Model-free RL algorithm"],
        ["Agent", "Decision-maker in RL system"],
        ["State (S)", "Current situation of environment"],
        ["Action (A)", "Choice taken by agent"],
        ["Reward (R)", "Feedback after action"],
    ]
    defs_table = Table(defs_data, colWidths=[1.5*inch, 4*inch])
    defs_table.setStyle(TableStyle([('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
                                    ('FONTSIZE', (0,0), (-1,-1), 9),
                                    ('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
    story.append(defs_table)
    
    story.append(PageBreak())
    
    # Section 2
    story.append(Paragraph("2. OVERALL DESCRIPTION", heading1_style))
    story.append(Paragraph("2.1 Product Perspective", heading2_style))
    story.append(Paragraph("The Household Grid Optimization using Reinforcement Learning system is a simulation-based software tool designed to demonstrate how AI can manage home energy.", normal_style))
    
    story.append(Paragraph("2.2 Product Functions", heading2_style))
    functions = [
        "1. Environment Simulation - Generates simulated data for electricity demand, temperature, and weather conditions.",
        "2. State Representation - Combines demand, temperature, and weather into a discrete state for the RL agent.",
        "3. RL Agent Decision Making - Uses Q-Learning algorithm to select the best action.",
        "4. Action Execution - Options: Grid Only, Solar Only, Generator Only, Grid+Solar Mixed.",
        "5. Reward Calculation - Based on demand satisfaction and energy cost.",
        "6. Learning and Optimization - Updates Q-table using Bellman equation.",
        "7. Performance Visualization - Graphs showing reward improvement over episodes.",
    ]
    for f in functions:
        story.append(Paragraph(f, normal_style))
    
    story.append(PageBreak())
    
    # Section 3 - System Architecture
    story.append(Paragraph("3. SYSTEM ARCHITECTURE", heading1_style))
    story.append(Paragraph("3.1 Architecture Overview", heading2_style))
    story.append(Paragraph("The system follows a modular architecture based on the standard Reinforcement Learning loop.", normal_style))
    
    # Architecture diagram as text
    arch_text = """
    ┌─────────────────┐         ┌─────────────────┐
    │   ENVIRONMENT   │ ──────> │    RL AGENT     │
    │ (Demand, Temp,  │  State   │  (Q-Learning)   │
    │    Weather)     │ <────── │                 │
    └─────────────────┘  Reward └────────┬────────┘
           ^                              │
           │                              │ Action
           │                              ▼
           │                       ┌─────────────────┐
           └───────────────────────│     EXECUTION   │
                     Next State    │   (Energy Source│
                                   │    Selection)   │
                                   └─────────────────┘
    """
    story.append(Paragraph(arch_text.replace('\n', '<br/>'), normal_style))
    
    story.append(Paragraph("3.2 Environment Module", heading2_style))
    story.append(Paragraph("This module simulates the household's energy context. Inputs include timestep and random seed. Output is a state vector [demand, temperature, weather_encoded].", normal_style))
    
    story.append(Paragraph("3.3 RL Agent Module (Q-Learning)", heading2_style))
    story.append(Paragraph("This is the core decision-making module using Q-Learning algorithm with parameters: Learning Rate (α)=0.1, Discount Factor (γ)=0.9, Exploration Rate (ε)=1.0 decaying to 0.01.", normal_style))
    
    story.append(PageBreak())
    
    # Section 5
    story.append(Paragraph("5. SYSTEM FEATURES", heading1_style))
    story.append(Paragraph("5.1 Environment Initialization", heading2_style))
    story.append(Paragraph("Sets up the simulation parameters and generates the initial state.", normal_style))
    
    story.append(Paragraph("5.2 State Generation", heading2_style))
    story.append(Paragraph("Creates a discrete state based on current demand, temperature, and weather. Total states = 3 (Demand) × 3 (Temperature) × 4 (Weather) = 36 states.", normal_style))
    
    story.append(Paragraph("5.3 Action Selection (Epsilon-Greedy)", heading2_style))
    story.append(Paragraph("The agent chooses an action based on the current Q-table. If random number < epsilon: Explore (random action). Else: Exploit (best known action).", normal_style))
    
    story.append(Paragraph("5.4 Reward and Next State Calculation", heading2_style))
    story.append(Paragraph("Calculates reward = +10 (demand satisfied) - Cost Penalty. Cost penalties: Solar=1, Grid=5, Generator=8.", normal_style))
    
    story.append(Paragraph("5.5 Q-Table Update (Learning)", heading2_style))
    story.append(Paragraph("Updates Q-values using Bellman equation: Q[s,a] = Q[s,a] + α * (reward + γ * max(Q[s_next]) - Q[s,a])", normal_style))
    
    story.append(Paragraph("5.6 Performance Visualization", heading2_style))
    story.append(Paragraph("Displays graphs showing total reward per episode and cost per episode using Matplotlib.", normal_style))
    
    story.append(PageBreak())
    
    # Section 6
    story.append(Paragraph("6. FUNCTIONAL REQUIREMENTS", heading1_style))
    fr_data = [
        ["FR1", "Environment Simulation", "Simulate demand, temperature, weather"],
        ["FR2", "State Discretization", "Convert continuous variables to discrete states"],
        ["FR3", "Q-Learning Algorithm", "Implement Q-Learning for training"],
        ["FR4", "Action Selection", "Select from 4 energy source actions"],
        ["FR5", "Reward Calculation", "Calculate reward based on cost and demand"],
        ["FR6", "Training Loop", "Run multiple episodes for learning"],
        ["FR7", "Q-Table Storage", "Save trained Q-table to file"],
        ["FR8", "Performance Graphing", "Generate reward and cost graphs"],
        ["FR9", "Parameter Configuration", "Configure learning rate, episodes"],
    ]
    fr_table = Table(fr_data, colWidths=[0.8*inch, 1.8*inch, 3*inch])
    fr_table.setStyle(TableStyle([('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
                                  ('FONTSIZE', (0,0), (-1,-1), 8),
                                  ('BACKGROUND', (0,0), (-1,0), colors.grey),
                                  ('GRID', (0,0), (-1,-1), 0.5, colors.black)]))
    story.append(fr_table)
    
    story.append(PageBreak())
    
    # Section 9
    story.append(Paragraph("9. NON-FUNCTIONAL REQUIREMENTS", heading1_style))
    story.append(Paragraph("9.1 Performance Requirements", heading2_style))
    story.append(Paragraph("The system should complete 1000 training episodes in under 1 minute on standard hardware.", normal_style))
    
    story.append(Paragraph("9.2 Usability Requirements", heading2_style))
    story.append(Paragraph("The system shall include a requirements.txt file and clear documentation.", normal_style))
    
    story.append(Paragraph("9.3 Reliability Requirements", heading2_style))
    story.append(Paragraph("Given the same random seed, the simulation shall produce identical results.", normal_style))
    
    story.append(PageBreak())
    
    # Section 11 & 12
    story.append(Paragraph("11. CONCLUSION", heading1_style))
    story.append(Paragraph("The Household Grid Optimization using Reinforcement Learning project presents a novel approach to managing home energy consumption. By applying a Q-Learning agent, the system learns to make intelligent decisions about which energy source to use based on real-time conditions. The simulation results demonstrate that the RL agent can successfully reduce costs compared to random or fixed-rule strategies.", normal_style))
    
    story.append(Paragraph("12. FUTURE ENHANCEMENTS", heading1_style))
    enhancements = [
        "1. Deep Reinforcement Learning (DRN) - Replace Q-table with Deep Q-Network",
        "2. Real-Time IoT Integration - Connect to smart meters and sensors",
        "3. Battery Storage Management - Add battery as additional action",
        "4. Multi-Home Optimization - Scale to manage neighborhood microgrid",
        "5. Predictive Modeling - Integrate LSTM for demand forecasting",
        "6. Mobile Application - Develop mobile dashboard for monitoring",
    ]
    for e in enhancements:
        story.append(Paragraph(e, normal_style))
    
    # Build PDF
    doc.build(story)
    print("PDF created successfully: Household_Grid_Optimization_SRS.pdf")

if __name__ == "__main__":
    create_srs_pdf()