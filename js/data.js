/* =========================================================
   CONTENT LAYER · js/data.js
   All content shown on the home page lives here.
   To change the site, edit this file — not the HTML.
   ========================================================= */
window.SITE = {

  /* ---------- Settings ---------- */
  config: {
    githubUser: 'zaidmuzaffar',
    // Formspree: create a free form at formspree.io and paste its ID (e.g. 'xyzabcd').
    formspreeId: 'xkjjljog',
    // GoatCounter: create a free site at goatcounter.com and paste its code (e.g. 'zaidmuzaffar').
    goatcounter: 'zaidmuzaffar'
  },

  /* ---------- Who I am ---------- */
  profile: {
    name: 'Zaid Muzaffar',
    role: 'Cloud & DevOps Engineer',
    email: 'zaidmuzaffar81@gmail.com',
    location: 'Peshawar, Pakistan',
    linkedin: 'https://www.linkedin.com/in/zaid-muzaffar-57329237a/',
    github: 'https://github.com/zaidmuzaffar',
    roles: ['Cloud & DevOps Engineer', 'CI/CD · Docker · Kubernetes', 'AWS: IAM · VPC · S3', 'Builder of AI that ships']
  },

  /* ---------- Page sections (drives nav, system map, palette, scroll progress) ---------- */
  sections: [
    { id: 'map',      num: '00', name: 'system map', title: 'System map',  service: 'Overview',   desc: 'how this site is laid out' },
    { id: 'about',    num: '01', name: 'about',      title: 'About me',    service: 'About',      desc: 'who I am' },
    { id: 'journey',  num: '02', name: 'journey',    title: 'Journey',     service: 'Journey',    desc: 'education & experience' },
    { id: 'projects', num: '03', name: 'projects',   title: 'Projects',    service: 'Projects',   desc: 'case studies & demos' },
    { id: 'stack',    num: '04', name: 'stack',      title: 'Stack',       service: 'Stack',      desc: 'skills & certifications' },
    { id: 'console',  num: '05', name: 'console',    title: 'Console',     service: 'Console',    desc: 'terminal & activity' },
    { id: 'contact',  num: '06', name: 'contact',    title: 'Contact',     service: 'Contact',    desc: 'say hello' }
  ],

  /* ---------- Quick facts (About) ---------- */
  facts: [
    { k: 'ROLE', v: 'Cloud & DevOps Engineer' },
    { k: 'DEGREE', v: 'BS Computer Science · 2026' },
    { k: 'UNIVERSITY', v: 'COMSATS Islamabad, Abbottabad' },
    { k: 'LANGUAGES', v: 'English · Urdu · Pashto' }
  ],

  /* ---------- Journey ---------- */
  timeline: [
    { when: '2021', title: 'Started BS Computer Science', text: 'COMSATS University Islamabad, Abbottabad Campus' },
    { when: 'during', title: 'Shipped my first production app', text: 'A full-stack web app on Firebase, used every day — see Projects' },
    { when: '2026', title: 'Final Year Project & graduation', text: 'Lawyer–Client Matching Web Platform · React, Node.js, MongoDB' },
    { when: '2026', title: 'IBM DevOps & Software Engineering track', text: 'Coursera: DevOps, Cloud Computing, Agile & Scrum, Software Engineering, Git & GitHub' },
    { when: 'now', title: 'Cloud & DevOps Engineer', text: 'CI/CD pipelines, Docker & Kubernetes, AWS (IAM, VPC, S3), infrastructure as code', now: true }
  ],

  /* ---------- Projects ---------- */
  filters: [
    { id: 'all', label: 'All' },
    { id: 'cloud', label: 'Cloud & DevOps' },
    { id: 'ai', label: 'AI' },
    { id: 'mobile', label: 'Mobile' },
    { id: 'web', label: 'Web' }
  ],
  projects: [
    {
      title: 'Star Pump House — Shop Management System', status: 'live', statusText: 'LIVE', cats: ['web', 'cloud', 'ai'],
      desc: 'The system a family hardware shop runs on every day: stock in units and feet, cash/credit sales, supplier and wholesale accounts, daily cash closing, profit reports, salesman logins and an AI assistant that answers in English or Roman Urdu.',
      stack: 'JavaScript · Firebase Auth · Firestore · Hosting · Gemini · App Check',
      demo: { email: 'demo@starpumphouse.com', password: 'Star123@' },
      links: [
        { label: 'Live demo ↗', href: 'https://starpumphouse.web.app', main: true },
        { label: 'Code ↗', href: 'https://github.com/zaidmuzaffar/star-pump-house' },
        { label: 'Case study →', href: 'projects/star-pump-house.html' },
        { label: 'PDF ↗', href: 'https://github.com/zaidmuzaffar/star-pump-house/blob/main/docs/Star_Pump_House_Full_Case_Study.pdf' }
      ]
    },
    {
      title: 'Vigil — Fall Detection & Live Location', status: 'build', statusText: 'IN BUILD', cats: ['mobile', 'ai', 'cloud'],
      desc: 'A safety app for everyone. An on-device neural network detects falls; if you don\'t answer "Are you okay?", your circle gets a full-screen alert with your live location. SOS, invite-link circles and helper tracking with ETA.',
      stack: 'Flutter · Firebase · TensorFlow Lite · 1D CNN · Colab',
      links: [
        { label: 'Case study →', href: 'projects/vigil.html', main: true },
        { label: 'Project site ↗', href: 'https://vigil-7fa6b.web.app' },
        { label: 'PDF ↓', href: 'docs/Vigil_Case_Study.pdf' }
      ]
    },
    {
      title: '"Mac" — Voice AI Assistant for macOS', status: 'build', statusText: 'IN BUILD', cats: ['ai'],
      desc: 'An always-on assistant that wakes on its name, talks back in Urdu or English, and actually controls the laptop: WhatsApp messages, YouTube, screenshots, volume — with spoken confirmation before anything destructive.',
      stack: 'Python · Gemini Live API · Ollama (Qwen 2.5 14B) · macOS automation',
      links: [
        { label: 'Case study →', href: 'projects/voice-assistant.html', main: true },
        { label: 'PDF ↓', href: 'docs/Voice_Assistant_Case_Study.pdf' }
      ]
    },
    {
      title: 'Linux System Administration Automation', status: 'done', statusText: 'DONE', cats: ['cloud'],
      desc: 'Modular Bash scripts that automate daily operations: user access management, environment setup, process monitoring, log parsing and health checks — version-controlled and documented in Git.',
      stack: 'Linux · Bash · Git & GitHub',
      links: [
        { label: 'Case study →', href: 'projects/linux-automation.html', main: true },
        { label: 'PDF ↓', href: 'docs/Linux_Automation_Case_Study.pdf' }
      ]
    },
    {
      title: 'Lawyer–Client Matching Platform', status: 'done', statusText: 'DONE · FYP', cats: ['web'],
      desc: 'Final year project: a web platform that matches clients with lawyers by expertise and search criteria, with MongoDB schemas, REST APIs and payment processing.',
      stack: 'React · Node.js · Express · MongoDB · REST',
      links: [
        { label: 'Case study →', href: 'projects/lawyer-client.html', main: true },
        { label: 'PDF ↓', href: 'docs/Lawyer_Client_Platform_Case_Study.pdf' }
      ]
    },
    {
      title: 'Roman-Urdu Scam Message Detector', status: 'next', statusText: 'NEXT', cats: ['ai'],
      desc: 'Detects scam SMS and WhatsApp messages written in Roman Urdu, with a built-in phishing link check. Next on the build list.',
      stack: 'Python · NLP', links: []
    },
    {
      title: 'Gesture Control', status: 'next', statusText: 'NEXT', cats: ['ai'],
      desc: 'Webcam hand tracking to control a laptop: air cursor, air click and trackpad-style swipes, on Mac and Windows.',
      stack: 'Computer vision', links: []
    }
  ],

  /* ---------- Stack ---------- */
  skills: [
    { group: 'CI/CD & AUTOMATION', items: ['CI/CD pipelines', 'GitHub Actions', 'Git & GitHub', 'Bash scripting', 'Agile / Scrum'] },
    { group: 'CONTAINERS & IaC', items: ['Docker', 'Containers', 'Docker Compose', 'Kubernetes', 'Terraform'] },
    { group: 'CLOUD (AWS)', items: ['IAM', 'VPC', 'S3', 'EC2', 'Route 53', 'Load Balancing & Auto Scaling'] },
    { group: 'SYSTEMS & NETWORKING', items: ['Linux administration', 'Networking (subnets, routing, DNS)', 'Firebase Hosting'] },
    { group: 'AI / ML', items: ['Python', 'TensorFlow Lite', 'Google Colab', 'Gemini API', 'Ollama'] },
    { group: 'WEB, DATA & MOBILE', items: ['JavaScript', 'React', 'Node.js', 'Express', 'Firestore', 'MongoDB', 'REST APIs', 'Flutter'] }
  ],
  certs: [
    { name: 'Introduction to DevOps', href: 'https://www.coursera.org/account/accomplishments/verify/ID5UOQ95D0QG' },
    { name: 'Introduction to Cloud Computing', href: 'https://www.coursera.org/account/accomplishments/verify/BLP5F4L1Z822' },
    { name: 'Agile Development and Scrum', href: 'https://www.coursera.org/account/accomplishments/verify/RV1DV08NWGEQ' },
    { name: 'Introduction to Software Engineering', href: 'https://www.coursera.org/account/accomplishments/verify/320E4Z1HD7JE' },
    { name: 'Getting Started with Git and GitHub', href: 'https://coursera.org/verify/EG8VQBHHNTO5' }
  ],
  certsIssuer: 'IBM DevOps & Software Engineering · Coursera',
  languages: [
    { name: 'English', level: 'C1 · proficient' },
    { name: 'Urdu', level: 'native' },
    { name: 'Pashto', level: 'native' }
  ],

  /* ---------- Recommendations ----------
     Add real quotes only, with the person's permission. The block stays hidden while this list is empty.
     Example: { quote: '…', name: 'Dr. Name', role: 'Head of CS, COMSATS Abbottabad' } */
  recommendations: [],

  /* ---------- System map: external services ---------- */
  external: [
    { name: 'GitHub', meta: 'source code', href: 'https://github.com/zaidmuzaffar' },
    { name: 'LinkedIn', meta: 'profile', href: 'https://www.linkedin.com/in/zaid-muzaffar-57329237a/' },
    { name: 'Live demos', meta: 'Firebase Hosting', href: 'https://starpumphouse.web.app' }
  ]
};
