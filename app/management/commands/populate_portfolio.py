from django.core.management.base import BaseCommand
from app.models import Skill, Project

class Command(BaseCommand):
    help = 'Populate the database with initial portfolio data'
                                
    def handle(self, *args, **options):
        self.stdout.write('==> Populating portfolio database...')
        
        # Create Skills
        skills_data = [
            # Programming Languages
            {'name': 'Python', 'category': 'programming', 'proficiency': 90, 'icon': '🐍', 'description': 'Advanced proficiency in Python for web development, automation, and data processing', 'order': 1},
            {'name': 'JavaScript', 'category': 'programming', 'proficiency': 80, 'icon': '⚡', 'description': 'Proficient in vanilla JavaScript and modern ES6+ features for interactive experiences', 'order': 4},
            {'name': 'HTML/CSS', 'category': 'programming', 'proficiency': 95, 'icon': '🎨', 'description': 'Expert in modern HTML5 and CSS3, including responsive design and animations', 'order': 3},
            
            # Frameworks & Libraries
            {'name': 'Django', 'category': 'framework', 'proficiency': 85, 'icon': '🎯', 'description': 'Skilled in Django framework for building robust, scalable web applications', 'order': 2},
            {'name': 'FastAPI', 'category': 'framework', 'proficiency': 75, 'icon': '⚡', 'description': 'Modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints', 'order': 8},
            {'name': 'LangChain', 'category': 'ai_ml', 'proficiency': 70, 'icon': '🔗', 'description': 'Framework for developing applications powered by language models and AI agents', 'order': 10},
            {'name': 'LangGraph', 'category': 'ai_ml', 'proficiency': 65, 'icon': '📊', 'description': 'Building stateful, multi-actor applications with LLMs using graph-based workflows', 'order': 11},
            {'name': 'LangSmith', 'category': 'ai_ml', 'proficiency': 68, 'icon': '🔍', 'description': 'Debugging, testing, and monitoring for LLM applications', 'order': 12},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 75, 'icon': '🐘', 'description': 'Database design and management with PostgreSQL for robust data solutions', 'order': 5},
            {'name': 'Redis', 'category': 'database', 'proficiency': 70, 'icon': '🔴', 'description': 'In-memory data structure store for caching, session management, and real-time applications', 'order': 9},
            
            # DevOps & Cloud
            {'name': 'Docker', 'category': 'devops', 'proficiency': 80, 'icon': '🐳', 'description': 'Containerization and deployment using Docker for scalable, portable applications', 'order': 7},
            {'name': 'AWS', 'category': 'devops', 'proficiency': 72, 'icon': '☁️', 'description': 'Amazon Web Services for cloud hosting, storage, and serverless computing', 'order': 13},
            {'name': 'Nginx', 'category': 'devops', 'proficiency': 75, 'icon': '🌐', 'description': 'Web server and reverse proxy for high-performance web applications', 'order': 14},
            
            # Tools & Technologies
            {'name': 'Git/GitHub', 'category': 'tools', 'proficiency': 88, 'icon': '📚', 'description': 'Version control expertise for collaborative development and project management', 'order': 6},
            {'name': 'Postman', 'category': 'tools', 'proficiency': 85, 'icon': '📮', 'description': 'API development and testing tool for building and testing REST APIs', 'order': 15},
            {'name': 'Celery', 'category': 'tools', 'proficiency': 73, 'icon': '🌿', 'description': 'Distributed task queue for Python applications with asynchronous processing', 'order': 16},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'[+] Created skill: {skill.name}')
            else:
                self.stdout.write(f'[*] Updated skill: {skill.name}')
                # Update existing skill with new data
                for key, value in skill_data.items():
                    setattr(skill, key, value)
                skill.save()
        
        # Create Sample Projects
        projects_data = [
            {
                'title': 'Notes App',
                'subtitle': 'Full-Featured Note-Taking Application',
                'short_description': 'A comprehensive web application built with Django and PostgreSQL, featuring user authentication, CRUD operations, and responsive design.',
                'description': '''
                A full-featured web application that demonstrates proficiency in backend development, database management, and user experience design.
                
                Key Features:
                - User authentication and authorization system
                - Complete CRUD operations for notes
                - Responsive design that works across all devices
                - Secure user account management
                - Clean and intuitive user interface
                
                Technical Implementation:
                - Built with Django framework for robust backend
                - PostgreSQL database for reliable data storage
                - Bootstrap for responsive frontend styling
                - Security best practices implemented
                ''',
                'github_url': 'https://github.com/mahendra-dhakal/Notes',
                'tech_tags': 'Django, PostgreSQL, Bootstrap, Python, HTML/CSS',
                'status': 'completed',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Portfolio Website',
                'subtitle': 'Cutting-Edge 2025 Design Portfolio',
                'short_description': 'This very website! Built with cutting-edge 2025 design principles, featuring advanced CSS animations, glassmorphism effects, and immersive user experiences.',
                'description': '''
                A showcase of modern web development techniques and attention to detail, representing the pinnacle of 2025 design trends.
                
                Design Features:
                - Holographic gradients with electric cyan, neon pink, and violet accents
                - Glassmorphism navigation with backdrop blur effects
                - Dynamic particle system with animated floating particles
                - 3D transforms and perspective effects throughout
                - Custom magnetic cursor with trailing effects
                
                Technical Features:
                - Django backend with dynamic content management
                - Advanced CSS with custom properties for dynamic theming
                - Intersection Observer API for performance-optimized animations
                - Responsive design with mobile-first approach
                - WCAG 2.1 AA accessibility compliance
                - SEO-optimized with semantic HTML
                ''',
                'tech_tags': 'Django, Advanced CSS, JavaScript, Responsive Design, Animation',
                'status': 'completed',
                'is_featured': True,
                'order': 2
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'[+] Created project: {project.title}')
            else:
                self.stdout.write(f'[*] Updated project: {project.title}')
        
        self.stdout.write(
            self.style.SUCCESS('==> Successfully populated portfolio database!')
        )