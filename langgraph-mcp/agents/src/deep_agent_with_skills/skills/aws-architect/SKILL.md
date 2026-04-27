---
name: aws-architect
description: Create comprehensive AWS architecture designs by taking user requirements, researching AWS official documentation and best practices, generating multiple solution options with trade-offs analysis, and producing detailed architecture documents with diagrams using the Draw.io skill. Use when users need AWS solution architecture, cloud infrastructure design, or AWS migration planning.
---

# AWS Architect Skill

## When to use this skill

Activate this skill when:
- A user asks for AWS solution architecture design or cloud infrastructure planning
- A user needs help designing AWS-based systems for specific use cases (web applications, data processing, microservices, etc.)
- A user wants to evaluate different AWS architectural approaches for their requirements
- A user needs migration strategies to AWS or modernization of existing applications
- A user requires detailed architecture documentation with diagrams for AWS implementations
- A user seeks guidance on AWS best practices, cost optimization, security, or performance considerations

## Core Principle

Follow AWS Well-Architected Framework principles while considering the specific user requirements, constraints, and goals. Research current AWS services, pricing, and best practices to provide accurate, up-to-date recommendations. Present multiple architectural options with clear trade-offs analysis to enable informed decision-making.

## Using Internet Search Tool

Before designing AWS architectures, use the Internet search tool to gather current information:

- **For AWS service documentation**: Search "AWS [service name] official documentation" or "AWS [service name] best practices 2024"
- **For architecture patterns**: Search "AWS architecture patterns [use case]" or "AWS reference architecture [industry]"
- **For pricing information**: Search "AWS pricing calculator [service]" or "AWS [service] cost optimization"
- **For security and compliance**: Search "AWS security best practices [use case]" or "AWS compliance [framework]"
- **For performance optimization**: Search "AWS performance optimization [service]" or "AWS [service] latency improvement"

Use search results to ensure recommendations are based on current AWS offerings and best practices. Cite sources appropriately in the architecture document.

## Structured Approach to AWS Architecture Design

### 0. Requirements Gathering and Research Preparation
- Clarify functional and non-functional requirements with the user
- Identify constraints (budget, timeline, team expertise, compliance requirements)
- Determine scale requirements (users, data volume, transaction rates)
- Identify integration requirements with existing systems
- Note any specific AWS service preferences or restrictions

### 1. Research Phase using Internet (Tavily) Search
- Search for AWS services relevant to the requirements
- Research AWS Well-Architected Framework pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization)
- Look for similar architecture patterns and reference implementations
- Find current pricing information and service limits
- Research security and compliance considerations
- Extract key facts, service capabilities, and best practices from results
- Note URLs and source titles for citations in the final document

### 2. Solution Design Options Development
Generate 2-3 distinct architectural approaches considering:

**Option A: Simplified/Cost-Optimized Approach**
- Uses managed services where appropriate to reduce operational overhead
- Focuses on cost-effective solutions
- May involve some trade-offs in performance or flexibility

**Option B: Standard/Balanced Approach**
- Follows AWS Well-Architected Framework recommendations
- Balances cost, performance, and operational considerations
- Uses appropriate mix of managed and customizable services

**Option C: Advanced/High-Performance Approach**
- Maximizes performance, scalability, and advanced features
- May involve higher complexity and cost
- Uses cutting-edge AWS services and architectures

For each option, analyze:
- **Architecture Overview**: High-level description and component diagram
- **Services Used**: Specific AWS services and their purposes
- **Data Flow**: How data moves through the system
- **Scalability**: How the solution handles growth
- **Security Considerations**: IAM, encryption, network security
- **Cost Implications**: Estimated monthly costs and cost drivers
- **Operational Complexity**: Management overhead and required expertise
- **Trade-offs**: Pros and cons compared to other options
- **When to Choose**: Specific scenarios where this option is optimal

### 3. Recommendation and Justification
- Select the recommended option based on user requirements and constraints
- Provide clear justification for the recommendation
- Note any assumptions made in the analysis
- Suggest potential evolution paths or future considerations

### 4. Detailed Architecture Document Creation
Create a comprehensive document including:

**Executive Summary**
- Brief overview of the problem and recommended solution
- Key benefits and expected outcomes

**Requirements Analysis**
- Functional requirements
- Non-functional requirements (performance, security, compliance, etc.)
- Constraints and assumptions

**Solution Options Comparison**
- Detailed comparison table of all options
- Trade-offs analysis for each option
- Cost comparison estimates

**Recommended Architecture**
- Detailed description of the chosen architecture
- Component-by-component breakdown
- Data flow explanation
- Security implementation details
- Monitoring and observability approach
- Disaster recovery and backup strategy

**Implementation Roadmap**
- Phased implementation approach
- Dependencies and prerequisites
- Estimated timeline and effort
- Skills and resources required

**Appendices**
- Detailed cost breakdown
- Service limits and quotas consideration
- Reference to AWS documentation sources
- Glossary of terms

### 5. Architecture Diagram Creation Using the Draw.io Skill

Use the `skills/drawio/SKILL.md` skill to create architecture diagrams as native `.drawio` files. This skill provides guidance on generating draw.io diagrams programmatically with optional export to PNG, SVG, or PDF formats.

#### 5.1 Diagram Types and When to Create Each

Create the following diagram types as appropriate for the architecture:

**High-Level Architecture Overview Diagram**
- Shows major AWS services and their relationships
- Displays data flow between components at a high level
- Includes external actors/users at edges
- Purpose: Provide a quick understanding of the overall solution
- Use early in the document after the architecture description

**Detailed Component Diagram**
- Breaks down each major service into sub-components
- Shows internal architecture of complex services
- Displays configuration and scaling details
- Purpose: Support detailed technical explanation
- Use when describing implementation specifics

**Data Flow Diagram**
- Shows how data enters, moves through, and exits the system
- Indicates data storage and processing steps
- Displays request/response patterns
- Purpose: Clarify data movement and transformations
- Use in dedicated "Data Flow" section

**Security and Network Diagram**
- Shows security group boundaries and network topology
- Displays IAM role associations
- Indicates encryption points and TLS connections
- Purpose: Clearly document security architecture
- Use in "Security Implementation" section

**Deployment Topology Diagram**
- Shows Amazon regions, availability zones, and deployment units
- Displays replication and failover relationships
- Indicates backup and disaster recovery setup
- Purpose: Clarify geographic distribution and redundancy
- Use in "Disaster Recovery and Backup" section

#### 5.2 Creating Diagrams Using the Draw.io Skill

Start diagram creation using the `/drawio` command. Refer to `skills/drawio/SKILL.md` for detailed instructions on diagram generation and export options.

**Command Format Examples:**

- `/drawio high-level architecture overview` → `high-level-architecture-overview.drawio`
- `/drawio png high-level architecture overview` → `high-level-architecture-overview.drawio.png`
- `/drawio svg data flow diagram` → `data-flow-diagram.drawio.svg`
- `/drawio pdf security and network topology` → `security-and-network-topology.drawio.pdf`

**Supported Export Formats:**
- `.drawio` (native format, editable)
- `.drawio.png` (PNG with embedded XML, editable in draw.io)
- `.drawio.svg` (SVG with embedded XML, editable in draw.io)
- `.drawio.pdf` (PDF with embedded XML, editable in draw.io)

**Key steps when creating diagrams:**
- Define objects/nodes: List all AWS services, databases, users, etc. that appear in the diagram
- Define connections: Specify relationships and data flows between objects
- Assign positions: Organize components logically (generally left-to-right or top-to-bottom data flow)
- Use AWS color coding and icon conventions for AWS services
- Choose an appropriate export format based on embedding and sharing requirements (PNG/SVG for web/documents, PDF for printing/formal documentation)

#### 5.3 Embedding Diagrams in the Architecture Document

Diagrams should be embedded directly in the markdown document for seamless reading:

1. **For Markdown Embedding**
   ```markdown
   ## [Section Title]

   [Section narrative text explaining the architecture/data flow/security model]

   ### Diagram: [Descriptive Title]

   ![AWS Architecture: High-Level Overview](aws-architecture-overview.svg)

   [Post-diagram explanation and key callouts]
   ```

2. **Diagram Organization**
   - Place diagram immediately after the relevant explanatory text
   - Include descriptive alt-text in markdown (helps with accessibility)
   - Use consistent naming: `aws-[use-case]-[diagram-type].svg`
   - Store all diagram files in an `./diagrams/` subdirectory relative to the document

3. **Referencing Diagrams in Text**
   - Create explicit references: "As shown in the diagram above, the data flows from..."
   - Number diagrams if document is long: "Figure 1: High-Level Architecture Overview"
   - Add callouts highlighting key components: "The primary data store (indicated in the diagram)"

#### 5.4 AWS Architecture Icons and Styling Guidelines

Follow these guidelines when creating diagrams:

- **AWS Service Icons**: Use official AWS service icons consistently
- **Color Coding**: 
  - User/Client: Light Blue
  - Compute: Orange
  - Database: Purple
  - Storage: Green
  - Network: Yellow
  - Security: Red accents
  - Integration: Gray
- **Connections**: Use arrows to show data flow direction; solid lines for synchronous, dashed for asynchronous
- **Grouping**: Use containers or layers to show AWS regions, VPCs, or security boundaries
- **Labels**: All connections should have descriptive labels (e.g., "HTTPS requests", "async events")
- **Legends**: Include a legend if using custom colors or symbols

#### 5.5 Quality Assurance for Diagrams

Before finalizing each diagram:

- **Accuracy**: Verify diagram matches the textual architecture description exactly
- **Completeness**: Ensure all components mentioned in text appear in the diagram
- **Clarity**: Check that connections and data flows are obvious and correctly labeled
- **Consistency**: Verify icons, colors, and styling match other diagrams in the document
- **Readability**: Ensure text is legible and components are not overcrowded
- **AWS Compliance**: Confirm use of official AWS icons and standard notations
- **Export Quality**: Verify SVG or PNG export maintains quality and is properly sized

## Output Format

The skill produces a comprehensive AWS architecture document in markdown format that includes:

1. **Document Header**: Title, date, version, and stakeholder information
2. **Table of Contents**: Auto-generated for easy navigation
3. **Main Sections**: As outlined in the structured approach above
4. **Architecture Diagrams**: **Embedded SVG diagrams** created with draw.io MCP server tools
   - Diagrams embedded directly within the markdown using `![alt-text](diagram-file.svg)` syntax
   - Each diagram placed immediately after its explanatory section
   - Descriptive figure captions and callouts highlighting key elements
   - All diagrams stored in `./diagrams/` subdirectory with consistent naming convention
   - Diagrams support all major markdown renderers and can be viewed in VS Code, GitHub, and documentation platforms
5. **References**: Proper citations to AWS documentation and other sources used
6. **Appendices**: Supporting information, calculations, and detailed specifications

The document should be suitable for presentation to technical stakeholders, architects, and implementation teams. The embedded diagrams ensure visual architecture understanding is maintained whether the document is viewed in markdown editors, GitHub repositories, or rendered in documentation systems.

## Using Citations Effectively

When referencing information from Internet(Tavily) searches:
- Use inline citations: "[Fact or recommendation] [1]"
- Maintain a numbered reference list at the end of the document
- Reference format: "[1] AWS Service Documentation: https://docs.aws.amazon.com/service/"
- Ensure all factual claims, service descriptions, and best practices are properly cited
- Prioritize official AWS documentation over third-party sources when possible

## Quality Assurance

Before finalizing the architecture document:
- Verify all AWS service names and capabilities are current
- Check that pricing information references are noted as estimates
- Ensure security recommendations align with AWS security best practices
- Confirm that the architecture follows Well-Architected Framework principles
- Validate that diagrams accurately represent the described architecture
- Review that trade-offs analysis is balanced and objective