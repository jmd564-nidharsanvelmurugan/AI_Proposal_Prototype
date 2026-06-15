<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Opportunity Discovery - Proposal Copilot</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "primary-fixed-dim": "#bec6e0",
                    "inverse-surface": "#2d3133",
                    "surface-container-lowest": "#ffffff",
                    "on-tertiary-fixed-variant": "#574425",
                    "on-secondary-fixed-variant": "#38485d",
                    "surface-bright": "#f7f9fb",
                    "surface-container": "#eceef0",
                    "on-primary-fixed-variant": "#3f465c",
                    "on-secondary-container": "#54647a",
                    "on-tertiary-fixed": "#271901",
                    "tertiary-fixed-dim": "#dec29a",
                    "secondary-fixed": "#d3e4fe",
                    "tertiary": "#000000",
                    "primary-container": "#131b2e",
                    "surface-container-high": "#e6e8ea",
                    "on-secondary": "#ffffff",
                    "inverse-primary": "#bec6e0",
                    "on-error": "#ffffff",
                    "on-tertiary": "#ffffff",
                    "surface": "#f7f9fb",
                    "on-error-container": "#93000a",
                    "primary-fixed": "#dae2fd",
                    "tertiary-fixed": "#fcdeb5",
                    "secondary-container": "#d0e1fb",
                    "surface-dim": "#d8dadc",
                    "on-tertiary-container": "#98805d",
                    "secondary-fixed-dim": "#b7c8e1",
                    "surface-tint": "#565e74",
                    "outline-variant": "#c6c6cd",
                    "tertiary-container": "#271901",
                    "outline": "#76777d",
                    "on-primary-fixed": "#131b2e",
                    "on-secondary-fixed": "#0b1c30",
                    "error": "#ba1a1a",
                    "inverse-on-surface": "#eff1f3",
                    "on-primary-container": "#7c839b",
                    "on-primary": "#ffffff",
                    "primary": "#000000",
                    "on-surface": "#191c1e",
                    "secondary": "#505f76",
                    "surface-container-highest": "#e0e3e5",
                    "on-background": "#191c1e",
                    "on-surface-variant": "#45464d",
                    "error-container": "#ffdad6",
                    "surface-container-low": "#f2f4f6",
                    "background": "#f7f9fb",
                    "surface-variant": "#e0e3e5"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "spacing": {
                    "gutter": "24px",
                    "md": "24px",
                    "xs": "8px",
                    "base": "4px",
                    "sm": "16px",
                    "xl": "80px",
                    "container-max": "1280px",
                    "lg": "48px"
            },
            "fontFamily": {
                    "headline-lg": ["Inter"],
                    "headline-md": ["Inter"],
                    "label-md": ["Inter"],
                    "label-sm": ["Inter"],
                    "body-md": ["Inter"],
                    "body-lg": ["Inter"],
                    "display-lg": ["Inter"],
                    "body-sm": ["Inter"]
            },
            "fontSize": {
                    "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                    "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                    "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                    "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                    "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                    "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f7f9fb;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #e2e8e0;
            border-radius: 10px;
        }
    </style>
</head>
<body class="bg-background text-on-surface">
<!-- Top Navigation Bar -->
<header class="fixed top-0 w-full z-50 bg-surface border-b border-outline-variant flex justify-between items-center px-lg h-16 max-w-container-max mx-auto left-0 right-0">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface">Proposal Copilot</span>
</div>
<nav class="hidden md:flex items-center gap-md h-full">
<a class="h-full flex items-center px-sm text-primary font-bold border-b-2 border-primary font-label-md text-label-md" href="#">Opportunity Discovery</a>
<a class="h-full flex items-center px-sm text-on-surface-variant hover:bg-surface-container transition-colors font-label-md text-label-md" href="#">Strategy Builder</a>
<a class="h-full flex items-center px-sm text-on-surface-variant hover:bg-surface-container transition-colors font-label-md text-label-md" href="#">Final Review</a>
</nav>
<div class="flex items-center gap-sm">
<button class="p-xs hover:bg-surface-container rounded-full transition-colors">
<span class="material-symbols-outlined text-primary">account_circle</span>
</button>
</div>
</header>
<!-- Main Content Canvas -->
<main class="pt-24 pb-32 px-lg max-w-container-max mx-auto min-h-screen">
<div class="grid grid-cols-1 lg:grid-cols-3 gap-gutter">
<!-- Left Column: Input & Metadata -->
<div class="lg:col-span-2 space-y-md">
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md">
<h2 class="font-headline-md text-headline-md mb-md">Opportunity Details</h2>
<div class="grid grid-cols-1 md:grid-cols-2 gap-sm mb-md">
<div>
<label class="block font-label-md text-label-md text-secondary mb-base">Client Name</label>
<input class="w-full bg-surface-container-low border-b-2 border-primary focus:ring-0 focus:border-primary border-none p-sm font-body-md text-body-md" placeholder="e.g. Acme Corp" type="text">
</div>
<div>
<label class="block font-label-md text-label-md text-secondary mb-base">Industry</label>
<select class="w-full bg-surface-container-low border-none p-sm font-body-md text-body-md focus:ring-0">
<option>Financial Services</option>
<option>Healthcare</option>
<option>Retail</option>
<option>Technology</option>
<option>Manufacturing</option>
</select>
</div>
<div>
<label class="block font-label-md text-label-md text-secondary mb-base">Solution Type</label>
<input class="w-full bg-surface-container-low border-none p-sm font-body-md text-body-md focus:ring-0" placeholder="e.g. Cloud Transformation" type="text">
</div>
<div>
<label class="block font-label-md text-label-md text-secondary mb-base">Project Category</label>
<select class="w-full bg-surface-container-low border-none p-sm font-body-md text-body-md focus:ring-0">
<option>Advisory</option>
<option>Implementation</option>
<option>Managed Services</option>
</select>
</div>
</div>
<div class="mb-md">
<label class="block font-label-md text-label-md text-secondary mb-base">Opportunity Description</label>
<textarea class="w-full bg-surface-container-low border-none p-sm font-body-md text-body-md focus:ring-0" placeholder="Describe the high-level business need..." rows="3"></textarea>
</div>
<div class="space-y-sm">
<label class="block font-label-md text-label-md text-secondary">Upload Discovery Documents</label>
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-xs">
<button class="flex flex-col items-center justify-center p-sm border border-dashed border-outline rounded-lg hover:bg-surface-container transition-all group">
<span class="material-symbols-outlined text-secondary mb-base group-hover:text-primary">description</span>
<span class="text-[10px] font-label-sm text-center">RFP Document</span>
</button>
<button class="flex flex-col items-center justify-center p-sm border border-dashed border-outline rounded-lg hover:bg-surface-container transition-all group">
<span class="material-symbols-outlined text-secondary mb-base group-hover:text-primary">quiz</span>
<span class="text-[10px] font-label-sm text-center">Sales Q&amp;A</span>
</button>
<button class="flex flex-col items-center justify-center p-sm border border-dashed border-outline rounded-lg hover:bg-surface-container transition-all group">
<span class="material-symbols-outlined text-secondary mb-base group-hover:text-primary">notes</span>
<span class="text-[10px] font-label-sm text-center">Discovery Notes</span>
</button>
<button class="flex flex-col items-center justify-center p-sm border border-dashed border-outline rounded-lg hover:bg-surface-container transition-all group">
<span class="material-symbols-outlined text-secondary mb-base group-hover:text-primary">groups</span>
<span class="text-[10px] font-label-sm text-center">MOM Document</span>
</button>
<button class="flex flex-col items-center justify-center p-sm border border-dashed border-outline rounded-lg hover:bg-surface-container transition-all group">
<span class="material-symbols-outlined text-secondary mb-base group-hover:text-primary">mic</span>
<span class="text-[10px] font-label-sm text-center">Transcript</span>
</button>
</div>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md relative overflow-hidden">
<div class="flex items-center gap-xs mb-sm">
<span class="material-symbols-outlined text-primary" style="font-variation-settings: 'FILL' 1;">auto_awesome</span>
<h3 class="font-label-md text-label-md uppercase tracking-widest text-primary">Intelligent Assistant</h3>
</div>
<div class="space-y-sm">
<p class="font-body-md text-body-md text-secondary">Brief the AI on specific nuances or requirements not captured in files.</p>
<div class="relative">
<input class="w-full bg-surface-container-low border-none p-md pr-16 rounded-lg font-body-md text-body-md focus:ring-2 focus:ring-primary-fixed-dim" placeholder="Client requires an AI chatbot. Azure deployment. Expected timeline four months." type="text">
<button class="absolute right-sm top-1/2 -translate-y-1/2 bg-primary text-on-primary p-xs rounded-lg hover:opacity-90">
<span class="material-symbols-outlined">send</span>
</button>
</div>
</div>
<!-- Ambient Glow Effect -->
<div class="absolute -right-12 -bottom-12 w-32 h-32 bg-primary-fixed-dim/20 blur-3xl pointer-events-none"></div>
</div>
</div>
<!-- Right Column: AI Extraction & Readiness -->
<div class="space-y-md">
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md">
<h3 class="font-label-md text-label-md text-secondary mb-md border-b border-outline-variant pb-xs">AI EXTRACTED INFO</h3>
<div class="space-y-sm custom-scrollbar max-h-[400px] overflow-y-auto pr-xs">
<div class="flex justify-between items-start py-xs border-b border-surface-container">
<span class="font-label-sm text-secondary">Client</span>
<span class="font-body-sm text-on-surface font-semibold">Acme Corp</span>
</div>
<div class="flex justify-between items-start py-xs border-b border-surface-container">
<span class="font-label-sm text-secondary">Industry</span>
<span class="font-body-sm text-on-surface">Financial Tech</span>
</div>
<div class="flex flex-col py-xs border-b border-surface-container">
<span class="font-label-sm text-secondary mb-xs">Business Problem</span>
<span class="font-body-sm text-on-surface">Legacy customer support systems resulting in high churn and low NPS scores.</span>
</div>
<div class="flex justify-between items-start py-xs border-b border-surface-container">
<span class="font-label-sm text-secondary">Timeline</span>
<span class="font-body-sm text-on-surface">4 Months</span>
</div>
<div class="flex justify-between items-start py-xs border-b border-surface-container">
<span class="font-label-sm text-secondary">Cloud Preference</span>
<span class="font-body-sm text-on-surface">Azure (Primary)</span>
</div>
<div class="flex flex-col py-xs border-b border-surface-container">
<span class="font-label-sm text-secondary mb-xs">Stakeholders</span>
<div class="flex flex-wrap gap-xs">
<span class="bg-surface-container px-xs py-[2px] rounded font-label-sm text-secondary">CTO</span>
<span class="bg-surface-container px-xs py-[2px] rounded font-label-sm text-secondary">CS Head</span>
</div>
</div>
<div class="flex justify-between items-start py-xs">
<span class="font-label-sm text-secondary">Project Objectives</span>
<span class="font-body-sm text-on-surface text-right">Cost Reduction, CX</span>
</div>
</div>
</div>
<!-- Readiness Card -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md shadow-sm">
<div class="flex justify-between items-center mb-md">
<h3 class="font-label-md text-label-md text-secondary">PROPOSAL READINESS</h3>
<span class="text-error font-label-md font-bold">65%</span>
</div>
<div class="w-full bg-surface-container-high h-1.5 rounded-full mb-lg overflow-hidden">
<div class="bg-error h-full" style="width: 65%;"></div>
</div>
<div class="space-y-sm">
<div class="flex items-center gap-sm p-sm bg-error-container/20 rounded-lg">
<span class="material-symbols-outlined text-error text-[20px]">warning</span>
<span class="font-label-sm text-on-error-container">Budget Information Missing</span>
</div>
<div class="flex items-center gap-sm p-sm bg-error-container/20 rounded-lg">
<span class="material-symbols-outlined text-error text-[20px]">warning</span>
<span class="font-label-sm text-on-error-container">Success Metrics Not Defined</span>
</div>
<div class="flex items-center gap-sm p-sm bg-error-container/20 rounded-lg">
<span class="material-symbols-outlined text-error text-[20px]">warning</span>
<span class="font-label-sm text-on-error-container">Support Model Undefined</span>
</div>
</div>
<button class="w-full mt-md py-sm border border-outline text-secondary font-label-md rounded-lg hover:bg-surface-container transition-colors">
                        Run Deeper Gap Analysis
                    </button>
</div>
<!-- Visual Asset / Image for Context -->
<div class="rounded-xl overflow-hidden h-48 relative border border-outline-variant">
<img class="w-full h-full object-cover" data-alt="A clean, professional workspace with a high-resolution laptop screen displaying complex data visualizations and proposal structures. The scene is shot in a bright, modern corporate environment with soft, natural light coming from large windows. Minimalist design elements include a sleek glass desk and a neutral-toned color palette of grays and blacks. The overall atmosphere is focused, efficient, and sophisticated." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDtReONpovCznB8l38Ptd7FfhWtQB2YjbVI7Nu3Ny5IYVXcUVdSpEkGwGoui9ZDMhslmo1t4d5N3AlOr_VCetECoocbi-XMJy8prtSEG6ErzS0hz_Bmv-k-033ulX_bsTYP_3pU9VvL8FVax-bnYBkfiKavYWlODRexuo-iFbPorK7iscUGEjJ7QBUhLAWQO-wV79SGnHGHccALsACQY-AtuFa62yZVySSp2Tlh09SzRY6j_bu3jN1R">
<div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-md">
<p class="text-white font-label-sm">System training on Acme RFP v2.4...</p>
</div>
</div>
</div>
</div>
</main>
<!-- Bottom Navigation Bar -->
<footer class="fixed bottom-0 left-0 right-0 w-full z-50 bg-surface-container-lowest border-t border-outline-variant flex justify-between items-center px-lg py-md max-w-container-max mx-auto shadow-md">
<div class="flex items-center gap-md">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
</div>
<div class="flex items-center">
<button class="flex items-center justify-center bg-primary text-on-primary rounded-xl px-lg py-sm hover:scale-95 duration-150 transition-all shadow-lg">
<span class="font-label-md text-label-md mr-xs">Continue</span>
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</div>
</footer>
<script>
        // Micro-interaction for inputs
        const inputs = document.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('focus', () => {
                input.parentElement.classList.add('scale-[1.01]');
                input.parentElement.style.transition = 'all 0.2s ease';
            });
            input.addEventListener('blur', () => {
                input.parentElement.classList.remove('scale-[1.01]');
            });
        });
    </script>
</body></html>








<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Proposal Copilot - Similar Proposal Discovery</title>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          "colors": {
            "primary-fixed-dim": "#bec6e0",
            "inverse-surface": "#2d3133",
            "surface-container-lowest": "#ffffff",
            "on-tertiary-fixed-variant": "#574425",
            "on-secondary-fixed-variant": "#38485d",
            "surface-bright": "#f7f9fb",
            "surface-container": "#eceef0",
            "on-primary-fixed-variant": "#3f465c",
            "on-secondary-container": "#54647a",
            "on-tertiary-fixed": "#271901",
            "tertiary-fixed-dim": "#dec29a",
            "secondary-fixed": "#d3e4fe",
            "tertiary": "#000000",
            "primary-container": "#131b2e",
            "surface-container-high": "#e6e8ea",
            "on-secondary": "#ffffff",
            "inverse-primary": "#bec6e0",
            "on-error": "#ffffff",
            "on-tertiary": "#ffffff",
            "surface": "#f7f9fb",
            "on-error-container": "#93000a",
            "primary-fixed": "#dae2fd",
            "tertiary-fixed": "#fcdeb5",
            "secondary-container": "#d0e1fb",
            "surface-dim": "#d8dadc",
            "on-tertiary-container": "#98805d",
            "secondary-fixed-dim": "#b7c8e1",
            "surface-tint": "#565e74",
            "outline-variant": "#c6c6cd",
            "tertiary-container": "#271901",
            "outline": "#76777d",
            "on-primary-fixed": "#131b2e",
            "on-secondary-fixed": "#0b1c30",
            "error": "#ba1a1a",
            "inverse-on-surface": "#eff1f3",
            "on-primary-container": "#7c839b",
            "on-primary": "#ffffff",
            "primary": "#000000",
            "on-surface": "#191c1e",
            "secondary": "#505f76",
            "surface-container-highest": "#e0e3e5",
            "on-background": "#191c1e",
            "on-surface-variant": "#45464d",
            "error-container": "#ffdad6",
            "surface-container-low": "#f2f4f6",
            "background": "#f7f9fb",
            "surface-variant": "#e0e3e5"
          },
          "borderRadius": {
            "DEFAULT": "0.125rem",
            "lg": "0.25rem",
            "xl": "0.5rem",
            "full": "0.75rem"
          },
          "spacing": {
            "gutter": "24px",
            "md": "24px",
            "xs": "8px",
            "base": "4px",
            "sm": "16px",
            "xl": "80px",
            "container-max": "1280px",
            "lg": "48px"
          },
          "fontFamily": {
            "headline-lg": ["Inter"],
            "headline-md": ["Inter"],
            "headline-lg-mobile": ["Inter"],
            "label-md": ["Inter"],
            "label-sm": ["Inter"],
            "body-md": ["Inter"],
            "body-lg": ["Inter"],
            "display-lg": ["Inter"],
            "body-sm": ["Inter"]
          },
          "fontSize": {
            "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
            "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
            "headline-lg-mobile": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
            "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
            "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
            "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
            "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
            "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
            "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
          }
        },
      },
    }
  </script>
<style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #F8FAFC;
    }
    .material-symbols-outlined {
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }
    /* Ambient Shadow from Design System */
    .ambient-shadow {
      box-shadow: 0px 4px 20px rgba(15, 23, 42, 0.05);
    }
    /* Horizontal Gutter separator */
    .vertical-gutter {
      border-left: 1px solid #E2E8F0;
    }
  </style>
</head>
<body class="bg-background text-on-surface">
<!-- TopAppBar from JSON -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">Proposal Copilot</span>
</div>
<div class="flex items-center gap-md">
<nav class="hidden md:flex gap-md">
<a class="font-label-md text-label-md text-primary dark:text-inverse-primary font-bold border-b-2 border-primary transition-colors" href="#">Library</a>
<a class="font-label-md text-label-md text-on-surface-variant dark:text-surface-variant hover:bg-surface-container dark:hover:bg-surface-container-highest transition-colors px-xs py-base rounded" href="#">Recent</a>
</nav>
<button class="material-symbols-outlined text-primary dark:text-inverse-primary">account_circle</button>
</div>
</header>
<!-- Main Content Layout -->
<main class="pt-24 pb-32 px-gutter max-w-container-max mx-auto">
<div class="grid grid-cols-1 lg:grid-cols-3 gap-lg">
<!-- Left Column: Proposal Discovery (2/3) -->
<section class="lg:col-span-2 space-y-md">
<header class="mb-lg">
<h1 class="font-headline-lg text-headline-lg text-primary mb-xs">Similar Proposals Found</h1>
<p class="font-body-md text-body-md text-secondary">We've identified historical documents that align with your current RFP requirements.</p>
</header>
<!-- Proposal Cards Container -->
<div class="space-y-sm">
<!-- Card 1: Healthcare AI Assistant -->
<article class="bg-surface-container-lowest border border-outline-variant rounded-xl p-sm ambient-shadow transition-all hover:border-primary">
<div class="flex justify-between items-start mb-sm">
<div>
<h3 class="font-headline-md text-headline-md text-primary mb-base">Healthcare AI Assistant</h3>
<div class="flex flex-wrap gap-xs">
<span class="bg-surface-container-high text-on-surface-variant px-xs py-base rounded-sm font-label-sm text-label-sm">Industry Match</span>
<span class="bg-surface-container-high text-on-surface-variant px-xs py-base rounded-sm font-label-sm text-label-sm">Solution Match</span>
<span class="bg-surface-container-high text-on-surface-variant px-xs py-base rounded-sm font-label-sm text-label-sm">Timeline Match</span>
</div>
</div>
<div class="text-right">
<span class="block font-display-lg text-headline-lg text-primary">96%</span>
<span class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Similarity</span>
</div>
</div>
<p class="font-body-md text-body-md text-on-surface-variant mb-md leading-relaxed">
              A comprehensive technical proposal for an enterprise-grade medical triage system utilizing conversational AI. Features modular security layers and HIPAA compliance documentation.
            </p>
<div class="flex flex-wrap gap-sm pt-sm border-t border-outline-variant">
<button class="flex items-center gap-xs px-sm h-[44px] bg-primary text-on-primary font-label-md text-label-md rounded-lg hover:opacity-80 transition-opacity">
<span class="material-symbols-outlined text-[20px]">visibility</span>
                Preview Proposal
              </button>
<button class="flex items-center gap-xs px-sm h-[44px] border border-primary text-primary font-label-md text-label-md rounded-lg hover:bg-surface-container transition-colors">
<span class="material-symbols-outlined text-[20px]">architecture</span>
                Use Proposal Structure
              </button>
</div>
</article>
<!-- Card 2: Financial Advisory Bot -->
<article class="bg-surface-container-lowest border border-outline-variant rounded-xl p-sm ambient-shadow transition-all hover:border-primary group">
<div class="flex justify-between items-center">
<div class="flex gap-sm items-center">
<div class="w-12 h-12 flex items-center justify-center bg-surface-container rounded-lg group-hover:bg-primary transition-colors">
<span class="material-symbols-outlined text-secondary group-hover:text-on-primary">account_balance</span>
</div>
<div>
<h3 class="font-headline-md text-headline-md text-primary">Financial Advisory Bot</h3>
<p class="font-body-sm text-body-sm text-secondary">Submitted: Oct 2023 • North America Region</p>
</div>
</div>
<div class="text-right">
<span class="block font-headline-lg text-headline-lg text-primary opacity-60">92%</span>
</div>
</div>
</article>
<!-- Card 3: Logistics Optimization -->
<article class="bg-surface-container-lowest border border-outline-variant rounded-xl p-sm ambient-shadow transition-all hover:border-primary group">
<div class="flex justify-between items-center">
<div class="flex gap-sm items-center">
<div class="w-12 h-12 flex items-center justify-center bg-surface-container rounded-lg group-hover:bg-primary transition-colors">
<span class="material-symbols-outlined text-secondary group-hover:text-on-primary">local_shipping</span>
</div>
<div>
<h3 class="font-headline-md text-headline-md text-primary">Logistics Optimization</h3>
<p class="font-body-sm text-body-sm text-secondary">Submitted: Jan 2024 • EMEA Region</p>
</div>
</div>
<div class="text-right">
<span class="block font-headline-lg text-headline-lg text-primary opacity-60">89%</span>
</div>
</div>
</article>
</div>
</section>
<!-- Right Column: Analysis Sidebar (1/3) -->
<aside class="lg:col-span-1">
<div class="sticky top-24 space-y-md">
<div class="bg-surface-container-low p-sm rounded-xl border border-outline-variant">
<div class="flex items-center gap-xs mb-sm">
<span class="material-symbols-outlined text-primary" style="font-variation-settings: 'FILL' 1;">insights</span>
<h2 class="font-label-md text-label-md text-primary uppercase tracking-widest">Why This Proposal Was Selected</h2>
</div>
<div class="space-y-sm">
<div class="flex justify-between items-center">
<span class="font-body-md text-body-md text-secondary">Industry Alignment</span>
<span class="font-label-md text-label-md text-primary">Strong</span>
</div>
<div class="w-full bg-outline-variant h-1 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[95%]"></div>
</div>
<div class="flex justify-between items-center">
<span class="font-body-md text-body-md text-secondary">Solution Complexity</span>
<span class="font-label-md text-label-md text-primary">Exact</span>
</div>
<div class="w-full bg-outline-variant h-1 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[100%]"></div>
</div>
<div class="flex justify-between items-center">
<span class="font-body-md text-body-md text-secondary">Contract Duration</span>
<span class="font-label-md text-label-md text-primary">High</span>
</div>
<div class="w-full bg-outline-variant h-1 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[82%]"></div>
</div>
</div>
<div class="mt-md pt-md border-t border-outline-variant">
<p class="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
                The AI identified these documents based on the **Health-Tech** domain and the **Natural Language Processing** requirements specified in your RFP upload. Using these structures typically improves win rates by **14%**.
              </p>
</div>
</div>
<!-- Decorative Graphic -->
<div class="relative h-48 rounded-xl overflow-hidden group">
<img class="w-full h-full object-cover grayscale transition-all group-hover:grayscale-0" data-alt="A professional, high-end visualization of data analytics on a sleek digital interface. The image features clean lines, a sophisticated dark navy and slate color palette, and subtle glowing data points that evoke a sense of corporate intelligence and trust. The style is minimalist and corporate modernism, with sharp focus and cinematic lighting that emphasizes clarity and efficiency." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDzUCQ-EUz3jCvys3-N_eAC4SpkvJc_Kzuertf4hJpuBJvithhgiQjSJeLQwCJMk1SdJB6Ojh6_70m9OnJQGYHA0fsZwf8ce3N5hOmj4oZ4fTCUanmWUVdDfOzfDWRguEECVjumL3VWI745oElCI-7Jd99wgD9DKIprDpSFvAtT16V1ySmco4sCv8JB0kGqSfFAu-yhTk18OjiTOZXbKtQTpknew197C1hr6LBG-EeIyL2P6_oNPrp7">
<div class="absolute inset-0 bg-primary/20 mix-blend-multiply"></div>
<div class="absolute bottom-sm left-sm text-white">
<span class="font-label-sm text-label-sm uppercase tracking-tighter opacity-80">Knowledge Base Insights</span>
<p class="font-headline-md text-headline-md leading-none">4.2k Documents Analyzed</p>
</div>
</div>
</div>
</aside>
</div>
</main>
<!-- BottomNavBar from JSON -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<div class="flex gap-sm">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
</div>
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="font-label-md text-label-md mr-xs">Continue</span>
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</footer>
<script>
    // Simple interaction to simulate card selection
    document.querySelectorAll('article').forEach(card => {
      card.addEventListener('click', function() {
        // Remove active state from others
        document.querySelectorAll('article').forEach(c => {
          c.classList.remove('ring-2', 'ring-primary');
        });
        // Add to this one
        this.classList.add('ring-2', 'ring-primary');
      });
    });
  </script>
</body></html>


<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Transcript Intelligence - Proposal Copilot</title>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&amp;display=swap" rel="stylesheet">
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-fixed-dim": "#bec6e0",
                        "inverse-surface": "#2d3133",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-fixed-variant": "#574425",
                        "on-secondary-fixed-variant": "#38485d",
                        "surface-bright": "#f7f9fb",
                        "surface-container": "#eceef0",
                        "on-primary-fixed-variant": "#3f465c",
                        "on-secondary-container": "#54647a",
                        "on-tertiary-fixed": "#271901",
                        "tertiary-fixed-dim": "#dec29a",
                        "secondary-fixed": "#d3e4fe",
                        "tertiary": "#000000",
                        "primary-container": "#131b2e",
                        "surface-container-high": "#e6e8ea",
                        "on-secondary": "#ffffff",
                        "inverse-primary": "#bec6e0",
                        "on-error": "#ffffff",
                        "on-tertiary": "#ffffff",
                        "surface": "#f7f9fb",
                        "on-error-container": "#93000a",
                        "primary-fixed": "#dae2fd",
                        "tertiary-fixed": "#fcdeb5",
                        "secondary-container": "#d0e1fb",
                        "surface-dim": "#d8dadc",
                        "on-tertiary-container": "#98805d",
                        "secondary-fixed-dim": "#b7c8e1",
                        "surface-tint": "#565e74",
                        "outline-variant": "#c6c6cd",
                        "tertiary-container": "#271901",
                        "outline": "#76777d",
                        "on-primary-fixed": "#131b2e",
                        "on-secondary-fixed": "#0b1c30",
                        "error": "#ba1a1a",
                        "inverse-on-surface": "#eff1f3",
                        "on-primary-container": "#7c839b",
                        "on-primary": "#ffffff",
                        "primary": "#000000",
                        "on-surface": "#191c1e",
                        "secondary": "#505f76",
                        "surface-container-highest": "#e0e3e5",
                        "on-background": "#191c1e",
                        "on-surface-variant": "#45464d",
                        "error-container": "#ffdad6",
                        "surface-container-low": "#f2f4f6",
                        "background": "#f7f9fb",
                        "surface-variant": "#e0e3e5"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "md": "24px",
                        "xs": "8px",
                        "base": "4px",
                        "sm": "16px",
                        "xl": "80px",
                        "container-max": "1280px",
                        "lg": "48px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "headline-lg-mobile": ["Inter"],
                        "label-md": ["Inter"],
                        "label-sm": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "headline-lg-mobile": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #E2E8F0;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #CBD5E1;
        }
    </style>
</head>
<body class="bg-background text-on-background font-body-md min-h-screen">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">Proposal Copilot</span>
</div>
<div class="flex items-center gap-md">
<nav class="hidden md:flex items-center gap-md h-full">
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container transition-colors px-xs py-base rounded" href="#">Drafts</a>
<a class="text-primary dark:text-inverse-primary font-bold border-b-2 border-primary font-label-md text-label-md px-xs py-base" href="#">Analysis</a>
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container transition-colors px-xs py-base rounded" href="#">Archive</a>
</nav>
<button class="material-symbols-outlined text-primary dark:text-inverse-primary p-xs hover:bg-surface-container transition-colors rounded-full" data-icon="account_circle">account_circle</button>
</div>
</header>
<!-- Main Content -->
<main class="pt-16 pb-24 px-md md:px-lg max-w-container-max mx-auto h-screen flex flex-col">
<!-- Header Section -->
<div class="py-md flex flex-col gap-xs">
<h1 class="font-headline-lg text-headline-lg text-primary">Transcript Intelligence</h1>
<p class="font-body-md text-body-md text-secondary">AI-driven extraction from your discovery sessions and RFP documentation.</p>
</div>
<!-- Content Grid (2/3 and 1/3 split) -->
<div class="flex-1 grid grid-cols-1 lg:grid-cols-3 gap-md min-h-0 overflow-hidden mb-sm">
<!-- Left Panel: Uploaded Transcript Preview -->
<section class="lg:col-span-2 flex flex-col bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden shadow-sm">
<div class="p-sm bg-surface-container-low border-b border-outline-variant flex justify-between items-center">
<span class="font-label-md text-label-md text-on-surface flex items-center gap-xs">
<span class="material-symbols-outlined text-[20px]" data-icon="description">description</span>
                        Discovery_Call_Transcript.txt
                    </span>
<span class="text-secondary font-label-sm text-label-sm">8:42 AM • 24 mins duration</span>
</div>
<div class="flex-1 overflow-y-auto p-lg font-body-md text-body-md leading-relaxed text-secondary selection:bg-primary-fixed">
<div class="space-y-md max-w-2xl mx-auto">
<p><strong class="text-on-surface">Interviewer (Sarah):</strong> Thanks for joining today, Michael. Let's dive into the core challenges your team is facing at <span class="bg-primary-fixed-dim/30 border-b-2 border-primary-fixed-dim px-1 text-on-primary-fixed font-medium">Acme Corp</span> regarding the new logistics platform.</p>
<p><strong class="text-on-surface">Michael:</strong> Of course. Basically, our current system can't handle the <span class="bg-primary-fixed-dim/30 border-b-2 border-primary-fixed-dim px-1 text-on-primary-fixed font-medium">peak seasonal load</span>, which results in significant delivery delays. We need a system that can <span class="bg-primary-fixed-dim/30 border-b-2 border-primary-fixed-dim px-1 text-on-primary-fixed font-medium">scale horizontally</span> and provide real-time visibility to our dispatchers.</p>
<p><strong class="text-on-surface">Sarah:</strong> Understood. What are the key milestones for this project?</p>
<p><strong class="text-on-surface">Michael:</strong> We need the MVP ready by <span class="bg-primary-fixed-dim/30 border-b-2 border-primary-fixed-dim px-1 text-on-primary-fixed font-medium">October 15th</span>. Our primary stakeholders are the VP of Logistics and the CTO, but the day-to-day operations team will be the end users.</p>
<p><strong class="text-on-surface">Sarah:</strong> And from a technical standpoint, are there specific requirements for the integration?</p>
<p><strong class="text-on-surface">Michael:</strong> Yes, it must integrate seamlessly with our existing <span class="bg-primary-fixed-dim/30 border-b-2 border-primary-fixed-dim px-1 text-on-primary-fixed font-medium">SAP ERP via REST APIs</span>. Security is also paramount, so SOC2 compliance is a non-negotiable for any vendor we partner with.</p>
<p><strong class="text-on-surface">Sarah:</strong> Have you allocated a specific budget range for the initial implementation phase?</p>
<p><strong class="text-on-surface">Michael:</strong> We're still finalizing the exact figures, but we expect it to be consistent with our standard enterprise modernization initiatives. We'll likely share more during the formal RFP response phase.</p>
<p><strong class="text-on-surface">Sarah:</strong> Fair enough. How will success be measured for this rollout?</p>
<p><strong class="text-on-surface">Michael:</strong> We'll be looking at throughput metrics, but we haven't mapped out the specific KPIs yet. We also need to discuss the long-term support model eventually.</p>
</div>
</div>
</section>
<!-- Right Panel: Extracted & Missing Info -->
<section class="flex flex-col gap-md">
<!-- Extracted Information -->
<div class="flex-1 bg-surface-container-lowest border border-outline-variant rounded-xl flex flex-col overflow-hidden shadow-sm">
<div class="p-sm bg-surface-container-low border-b border-outline-variant">
<span class="font-label-md text-label-md text-on-surface flex items-center gap-xs">
<span class="material-symbols-outlined text-[20px]" data-icon="auto_awesome">auto_awesome</span>
                            Extracted Information
                        </span>
</div>
<div class="flex-1 overflow-y-auto p-sm space-y-sm">
<div class="group p-xs rounded-lg hover:bg-surface-container transition-colors">
<label class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Client Name</label>
<p class="font-body-md text-on-surface">Acme Corp</p>
</div>
<div class="group p-xs rounded-lg hover:bg-surface-container transition-colors">
<label class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Business Challenges</label>
<p class="font-body-md text-on-surface">Peak seasonal load handling, delivery delays in current system.</p>
</div>
<div class="group p-xs rounded-lg hover:bg-surface-container transition-colors">
<label class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Project Objectives</label>
<p class="font-body-md text-on-surface">Horizontal scaling, real-time dispatcher visibility.</p>
</div>
<div class="group p-xs rounded-lg hover:bg-surface-container transition-colors">
<label class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Timeline</label>
<p class="font-body-md text-on-surface">MVP deadline: October 15th</p>
</div>
<div class="group p-xs rounded-lg hover:bg-surface-container transition-colors">
<label class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Stakeholders</label>
<p class="font-body-md text-on-surface">VP of Logistics, CTO, Operations Team</p>
</div>
<div class="group p-xs rounded-lg hover:bg-surface-container transition-colors">
<label class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Budget References</label>
<p class="font-body-md text-on-surface">Enterprise modernization standard (Pending RFP).</p>
</div>
<div class="group p-xs rounded-lg hover:bg-surface-container transition-colors">
<label class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Technical Requirements</label>
<p class="font-body-md text-on-surface">SAP ERP integration, REST APIs, SOC2 Compliance.</p>
</div>
</div>
</div>
<!-- Missing Information -->
<div class="bg-error-container/10 border border-error/20 rounded-xl overflow-hidden shadow-sm">
<div class="p-sm bg-error-container/20 border-b border-error/10">
<span class="font-label-md text-label-md text-error flex items-center gap-xs">
<span class="material-symbols-outlined text-[20px]" data-icon="warning">warning</span>
                            Missing Information
                        </span>
</div>
<div class="p-sm space-y-xs">
<div class="flex items-center gap-xs text-on-surface-variant py-xs border-b border-outline-variant/30 last:border-0">
<span class="material-symbols-outlined text-[18px] text-error" data-icon="close">close</span>
<span class="font-body-sm text-body-sm">Budget (Specific Figures)</span>
</div>
<div class="flex items-center gap-xs text-on-surface-variant py-xs border-b border-outline-variant/30 last:border-0">
<span class="material-symbols-outlined text-[18px] text-error" data-icon="close">close</span>
<span class="font-body-sm text-body-sm">Success Metrics / KPIs</span>
</div>
<div class="flex items-center gap-xs text-on-surface-variant py-xs border-b border-outline-variant/30 last:border-0">
<span class="material-symbols-outlined text-[18px] text-error" data-icon="close">close</span>
<span class="font-body-sm text-body-sm">Support Model</span>
</div>
</div>
</div>
</section>
</div>
</main>
<!-- BottomNavBar -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all rounded-xl gap-xs">
<span class="material-symbols-outlined" data-icon="arrow_back">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<div class="flex gap-sm">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all rounded-xl gap-xs">
<span class="material-symbols-outlined" data-icon="close">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-lg py-xs hover:opacity-90 active:scale-95 duration-150 gap-xs">
<span class="font-label-md text-label-md">Continue</span>
<span class="material-symbols-outlined" data-icon="arrow_forward">arrow_forward</span>
</button>
</div>
</footer>
<!-- Atmosphere Micro-interaction script -->
<script>
        // Simple logic to simulate text highlight clicking in transcript
        document.querySelectorAll('.bg-primary-fixed-dim\\/30').forEach(highlight => {
            highlight.style.cursor = 'pointer';
            highlight.addEventListener('mouseover', () => {
                highlight.style.backgroundColor = 'rgba(190, 198, 224, 0.6)';
            });
            highlight.addEventListener('mouseout', () => {
                highlight.style.backgroundColor = 'rgba(190, 198, 224, 0.3)';
            });
        });
    </script>
</body></html>


<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Proposal Preview - Proposal Copilot</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-fixed-dim": "#bec6e0",
                        "inverse-surface": "#2d3133",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-fixed-variant": "#574425",
                        "on-secondary-fixed-variant": "#38485d",
                        "surface-bright": "#f7f9fb",
                        "surface-container": "#eceef0",
                        "on-primary-fixed-variant": "#3f465c",
                        "on-secondary-container": "#54647a",
                        "on-tertiary-fixed": "#271901",
                        "tertiary-fixed-dim": "#dec29a",
                        "secondary-fixed": "#d3e4fe",
                        "tertiary": "#000000",
                        "primary-container": "#131b2e",
                        "surface-container-high": "#e6e8ea",
                        "on-secondary": "#ffffff",
                        "inverse-primary": "#bec6e0",
                        "on-error": "#ffffff",
                        "on-tertiary": "#ffffff",
                        "surface": "#f7f9fb",
                        "on-error-container": "#93000a",
                        "primary-fixed": "#dae2fd",
                        "tertiary-fixed": "#fcdeb5",
                        "secondary-container": "#d0e1fb",
                        "surface-dim": "#d8dadc",
                        "on-tertiary-container": "#98805d",
                        "secondary-fixed-dim": "#b7c8e1",
                        "surface-tint": "#565e74",
                        "outline-variant": "#c6c6cd",
                        "tertiary-container": "#271901",
                        "outline": "#76777d",
                        "on-primary-fixed": "#131b2e",
                        "on-secondary-fixed": "#0b1c30",
                        "error": "#ba1a1a",
                        "inverse-on-surface": "#eff1f3",
                        "on-primary-container": "#7c839b",
                        "on-primary": "#ffffff",
                        "primary": "#000000",
                        "on-surface": "#191c1e",
                        "secondary": "#505f76",
                        "surface-container-highest": "#e0e3e5",
                        "on-background": "#191c1e",
                        "on-surface-variant": "#45464d",
                        "error-container": "#ffdad6",
                        "surface-container-low": "#f2f4f6",
                        "background": "#f7f9fb",
                        "surface-variant": "#e0e3e5"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "md": "24px",
                        "xs": "8px",
                        "base": "4px",
                        "sm": "16px",
                        "xl": "80px",
                        "container-max": "1280px",
                        "lg": "48px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "headline-lg-mobile": ["Inter"],
                        "label-md": ["Inter"],
                        "label-sm": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "headline-lg-mobile": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        body { font-family: 'Inter', sans-serif; }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #e2e8f0; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #cbd5e1; }
        .document-shadow { box-shadow: 0px 4px 20px rgba(15, 23, 42, 0.05); }
    </style>
</head>
<body class="bg-background text-on-background min-h-screen">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface border-b border-outline-variant">
<div class="font-headline-md text-headline-md font-bold text-on-surface">Proposal Copilot</div>
<div class="flex items-center gap-md">
<button class="material-symbols-outlined text-on-surface-variant hover:bg-surface-container transition-colors p-xs rounded-full">account_circle</button>
</div>
</header>
<main class="pt-16 pb-24 max-w-container-max mx-auto h-screen flex overflow-hidden">
<!-- Left Side: Proposal Preview (2/3) -->
<section class="w-2/3 flex flex-col h-full border-r border-outline-variant bg-surface-bright">
<div class="p-md flex justify-between items-center border-b border-outline-variant bg-white">
<h1 class="font-headline-md text-headline-md text-primary">Proposal Preview</h1>
<div class="flex gap-xs">
<span class="bg-surface-container text-on-surface-variant px-sm py-1 font-label-sm text-label-sm rounded-lg flex items-center gap-1">
<span class="material-symbols-outlined text-[16px]">description</span> Draft_v2.4.docx
                    </span>
</div>
</div>
<!-- Scrollable Content -->
<div class="flex-1 overflow-y-auto p-lg bg-surface-container-low">
<div class="max-w-[800px] mx-auto bg-white p-xl document-shadow rounded-lg space-y-lg border border-outline-variant">
<!-- Executive Summary -->
<div class="space-y-sm" id="section-exec">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Executive Summary</h2>
<p class="font-body-md text-body-md text-secondary leading-relaxed">
                            This proposal outlines the strategic framework for the Digital Transformation initiative of Global Logistics Corp. Our objective is to streamline supply chain operations through integrated AI-driven forecasting and real-time inventory management.
                        </p>
</div>
<!-- Business Context -->
<div class="space-y-sm" id="section-context">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Business Context</h2>
<p class="font-body-md text-body-md text-secondary leading-relaxed">
                            Global Logistics Corp operates across 45 countries, managing over 1,200 distribution nodes. Recent market shifts have exposed vulnerabilities in legacy tracking systems, leading to a 14% increase in operational latency over the last fiscal year.
                        </p>
</div>
<!-- Current Challenges -->
<div class="space-y-sm" id="section-challenges">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Current Challenges</h2>
<ul class="list-disc pl-md space-y-xs font-body-md text-body-md text-secondary">
<li>Manual reconciliation of cross-border customs documentation.</li>
<li>Inaccurate predictive maintenance causing unscheduled fleet downtime.</li>
<li>Fragmented data silos between regional headquarters.</li>
</ul>
</div>
<!-- Proposed Solution -->
<div class="space-y-sm" id="section-solution">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Proposed Solution</h2>
<div class="bg-surface-container-low p-md border-l-4 border-primary rounded-r-lg italic font-body-md text-body-md text-secondary">
                            "The implementation of the Nexus AI Core will serve as the centralized nervous system for all logistics operations, providing end-to-end visibility."
                        </div>
</div>
<!-- Architecture -->
<div class="space-y-sm" id="section-arch">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Architecture</h2>
<img class="w-full h-64 object-cover rounded-lg border border-outline-variant" data-alt="A clean, minimalist technical diagram showing a cloud computing architecture with interconnected servers and data flow lines. The style is professional and corporate, using a palette of white, slate grays, and deep navy accents. The lighting is soft and even, emphasizing clarity and structured design in a high-tech corporate environment." src="https://lh3.googleusercontent.com/aida-public/AB6AXuB_48LuOxkR5rQSqL9V2B9GG9sQwz_rCUH7oabi3ZGFtaEnvjBd-l6HhkzLdhRRAPvINAbIgrD23bLa04Hblg_H56Vk37njguinR-hRcPpY-Ow-yWceEJZV9VNrc83pTHRD996kRNwtrOEdirrsKk-k91mo5jevU1FQyF1hjWMUr_K94oauTvIxbsIHzHTasmJSKFnVE9GHwub2_5_RR9K3tLpNytWkaJ1LZd74F4mtQ1wyWMRvpkHY">
</div>
<!-- Implementation Plan -->
<div class="space-y-sm" id="section-plan">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Implementation Plan</h2>
<p class="font-body-md text-body-md text-secondary leading-relaxed">
                            The transition will occur over a three-phase rollout: Discovery &amp; Mapping (4 weeks), Pilot Integration (8 weeks), and Global Scaling (12 weeks).
                        </p>
</div>
<!-- Pricing -->
<div class="space-y-sm" id="section-pricing">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Pricing</h2>
<div class="grid grid-cols-2 gap-md pt-sm">
<div class="p-md border border-outline-variant rounded-lg">
<span class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Phase 1 Total</span>
<div class="font-headline-md text-headline-md text-primary mt-1">$450,000</div>
</div>
<div class="p-md border border-outline-variant rounded-lg">
<span class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Estimated ROI</span>
<div class="font-headline-md text-headline-md text-primary mt-1">215%</div>
</div>
</div>
</div>
<!-- Risks -->
<div class="space-y-sm" id="section-risks">
<h2 class="font-headline-md text-headline-md text-primary border-b border-outline-variant pb-2">Risks</h2>
<p class="font-body-md text-body-md text-secondary leading-relaxed">
                            Potential risks include data migration delays and regional compliance variations. Mitigation strategies involve parallel system runs and dedicated legal task forces.
                        </p>
</div>
</div>
</div>
</section>
<!-- Right Side: Extracted Structure (1/3) -->
<aside class="w-1/3 flex flex-col h-full bg-surface">
<div class="p-md border-b border-outline-variant bg-white">
<h3 class="font-headline-md text-headline-md text-primary">Extracted Structure</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1">Found 8 core sections to replicate.</p>
</div>
<!-- Recommendation Box -->
<div class="p-md">
<div class="bg-primary-container p-md rounded-xl border border-primary-fixed-dim">
<div class="flex items-start gap-sm">
<div class="p-xs bg-primary text-on-primary rounded-lg">
<span class="material-symbols-outlined">auto_awesome</span>
</div>
<div class="flex-1">
<h4 class="font-label-md text-label-md text-primary-fixed-dim uppercase tracking-wider">AI Recommendation</h4>
<p class="font-body-md text-body-md text-white mt-1">
                                This proposal has a <span class="text-emerald-400 font-bold">96% similarity score</span> and is recommended as the baseline structure.
                            </p>
</div>
</div>
</div>
</div>
<!-- Vertical List -->
<nav class="flex-1 overflow-y-auto px-md pb-md space-y-xs">
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">01</span>
<span class="font-label-md text-label-md text-primary">Executive Summary</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">02</span>
<span class="font-label-md text-label-md text-primary">Business Context</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">03</span>
<span class="font-label-md text-label-md text-primary">Current Challenges</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">04</span>
<span class="font-label-md text-label-md text-primary">Proposed Solution</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">05</span>
<span class="font-label-md text-label-md text-primary">Architecture</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">06</span>
<span class="font-label-md text-label-md text-primary">Implementation Plan</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">07</span>
<span class="font-label-md text-label-md text-primary">Pricing</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
<div class="p-sm flex items-center justify-between bg-white border border-outline-variant rounded-lg hover:bg-surface-container transition-all cursor-pointer group">
<div class="flex items-center gap-sm">
<span class="font-label-md text-label-md text-secondary group-hover:text-primary transition-colors">08</span>
<span class="font-label-md text-label-md text-primary">Risks</span>
</div>
<span class="material-symbols-outlined text-emerald-500 font-variation-settings-'FILL'-1 text-[18px]">check_circle</span>
</div>
</nav>
<!-- Sidebar Actions -->
<div class="p-md bg-white border-t border-outline-variant space-y-sm">
<button class="w-full flex items-center justify-center gap-xs bg-primary text-on-primary py-sm font-label-md text-label-md rounded-lg hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined text-[20px]">copy_all</span>
                    Use Structure
                </button>
<button class="w-full flex items-center justify-center gap-xs bg-surface-container-high text-on-surface py-sm font-label-md text-label-md rounded-lg hover:bg-surface-container-highest transition-colors">
<span class="material-symbols-outlined text-[20px]">compare_arrows</span>
                    Compare Proposal
                </button>
</div>
</aside>
</main>
<!-- BottomNavBar -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest border-t border-outline-variant shadow-md">
<div class="flex gap-md">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-2">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-2">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
</div>
<button class="flex items-center justify-center bg-primary text-on-primary rounded-xl px-lg py-sm hover:opacity-80 transition-opacity active:scale-95 duration-150">
<span class="font-label-md text-label-md mr-2">Continue</span>
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</footer>
<script>
        // Micro-interactions for scrolling and side-navigation highlighting
        const scrollContainer = document.querySelector('.overflow-y-auto');
        const sections = ['exec', 'context', 'challenges', 'solution', 'arch', 'plan', 'pricing', 'risks'];
        const navItems = document.querySelectorAll('aside nav > div');

        scrollContainer.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(id => {
                const element = document.getElementById('section-' + id);
                const rect = element.getBoundingClientRect();
                if (rect.top < 300) {
                    current = id;
                }
            });

            navItems.forEach((item, index) => {
                const label = item.querySelector('span:nth-child(2)').textContent.toLowerCase();
                const sectionName = sections[index];
                if (label.includes(sectionName.replace('exec', 'executive')) || sectionName.includes(label.split(' ')[0])) {
                   // item.classList.add('bg-primary-container');
                } else {
                   // item.classList.remove('bg-primary-container');
                }
            });
        });
    </script>
</body></html>


<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Proposal Structure Builder - Proposal Copilot</title>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&amp;display=swap" rel="stylesheet">
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Tailwind Config -->
<script id="tailwind-config">
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          "colors": {
            "primary-fixed-dim": "#bec6e0",
            "inverse-surface": "#2d3133",
            "surface-container-lowest": "#ffffff",
            "on-tertiary-fixed-variant": "#574425",
            "on-secondary-fixed-variant": "#38485d",
            "surface-bright": "#f7f9fb",
            "surface-container": "#eceef0",
            "on-primary-fixed-variant": "#3f465c",
            "on-secondary-container": "#54647a",
            "on-tertiary-fixed": "#271901",
            "tertiary-fixed-dim": "#dec29a",
            "secondary-fixed": "#d3e4fe",
            "tertiary": "#000000",
            "primary-container": "#131b2e",
            "surface-container-high": "#e6e8ea",
            "on-secondary": "#ffffff",
            "inverse-primary": "#bec6e0",
            "on-error": "#ffffff",
            "on-tertiary": "#ffffff",
            "surface": "#f7f9fb",
            "on-error-container": "#93000a",
            "primary-fixed": "#dae2fd",
            "tertiary-fixed": "#fcdeb5",
            "secondary-container": "#d0e1fb",
            "surface-dim": "#d8dadc",
            "on-tertiary-container": "#98805d",
            "secondary-fixed-dim": "#b7c8e1",
            "surface-tint": "#565e74",
            "outline-variant": "#c6c6cd",
            "tertiary-container": "#271901",
            "outline": "#76777d",
            "on-primary-fixed": "#131b2e",
            "on-secondary-fixed": "#0b1c30",
            "error": "#ba1a1a",
            "inverse-on-surface": "#eff1f3",
            "on-primary-container": "#7c839b",
            "on-primary": "#ffffff",
            "primary": "#000000",
            "on-surface": "#191c1e",
            "secondary": "#505f76",
            "surface-container-highest": "#e0e3e5",
            "on-background": "#191c1e",
            "on-surface-variant": "#45464d",
            "error-container": "#ffdad6",
            "surface-container-low": "#f2f4f6",
            "background": "#f7f9fb",
            "surface-variant": "#e0e3e5"
          },
          "borderRadius": {
            "DEFAULT": "0.125rem",
            "lg": "0.25rem",
            "xl": "0.5rem",
            "full": "0.75rem"
          },
          "spacing": {
            "gutter": "24px",
            "md": "24px",
            "xs": "8px",
            "base": "4px",
            "sm": "16px",
            "xl": "80px",
            "container-max": "1280px",
            "lg": "48px"
          },
          "fontFamily": {
            "headline-lg": ["Inter"],
            "headline-md": ["Inter"],
            "headline-lg-mobile": ["Inter"],
            "label-md": ["Inter"],
            "label-sm": ["Inter"],
            "body-md": ["Inter"],
            "body-lg": ["Inter"],
            "display-lg": ["Inter"],
            "body-sm": ["Inter"]
          },
          "fontSize": {
            "headline-lg": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
            "headline-md": ["24px", { "lineHeight": "32px", "fontWeight": "600" }],
            "headline-lg-mobile": ["24px", { "lineHeight": "32px", "fontWeight": "600" }],
            "label-md": ["14px", { "lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600" }],
            "label-sm": ["12px", { "lineHeight": "16px", "fontWeight": "500" }],
            "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
            "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
            "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
            "body-sm": ["14px", { "lineHeight": "20px", "fontWeight": "400" }]
          }
        },
      },
    }
  </script>
<style>
    body {
      background-color: #f7f9fb;
      font-family: 'Inter', sans-serif;
    }
    .material-symbols-outlined {
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }
    .drag-handle:hover {
      cursor: grab;
    }
    .drag-handle:active {
      cursor: grabbing;
    }
    .sortable-ghost {
      opacity: 0.4;
      background: #e2e8f0;
    }
  </style>
</head>
<body class="bg-background text-on-surface">
<!-- TopAppBar from JSON -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="flex items-center gap-sm">
<div class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">Proposal Copilot</div>
</div>
<nav class="hidden md:flex gap-md items-center h-full">
<a class="h-full flex items-center px-xs text-on-surface-variant dark:text-surface-variant hover:bg-surface-container dark:hover:bg-surface-container-highest transition-colors font-label-md text-label-md" href="#">Dashboard</a>
<a class="h-full flex items-center px-xs text-primary dark:text-inverse-primary font-bold border-b-2 border-primary hover:bg-surface-container dark:hover:bg-surface-container-highest transition-colors font-label-md text-label-md" href="#">Structure</a>
<a class="h-full flex items-center px-xs text-on-surface-variant dark:text-surface-variant hover:bg-surface-container dark:hover:bg-surface-container-highest transition-colors font-label-md text-label-md" href="#">Library</a>
</nav>
<div class="flex items-center gap-sm">
<button class="material-symbols-outlined text-primary dark:text-inverse-primary hover:bg-surface-container transition-colors p-xs rounded-full">account_circle</button>
</div>
</header>
<!-- Main Content Canvas -->
<main class="pt-24 pb-32 px-md md:px-lg max-w-container-max mx-auto min-h-screen">
<div class="max-w-4xl mx-auto">
<!-- Page Header -->
<div class="mb-lg flex flex-col md:flex-row md:items-end justify-between gap-md">
<div>
<h1 class="font-headline-lg text-headline-lg text-primary mb-xs">Structure Builder</h1>
<p class="font-body-md text-body-md text-secondary">Define the narrative flow of your proposal. Reorder sections or add new custom modules.</p>
</div>
<button class="flex items-center gap-xs px-sm py-xs bg-primary text-on-primary rounded-xl hover:opacity-80 transition-opacity font-label-md text-label-md">
<span class="material-symbols-outlined">add</span>
          Add Section
        </button>
</div>
<!-- Workspace Area: Reorderable List -->
<div class="space-y-sm" id="section-list">
<!-- Section Item -->
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">description</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Executive Summary</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">business_center</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Business Context</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">report_problem</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Current Challenges</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">lightbulb</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Proposed Solution</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">architecture</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Technical Architecture</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">event_available</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Implementation Plan</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">groups</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Team Structure</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">payments</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Pricing</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">rule</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Assumptions</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
<div class="group flex items-center gap-md bg-surface-container-lowest border border-outline-variant p-sm rounded-xl transition-all hover:shadow-md">
<div class="drag-handle flex items-center text-outline">
<span class="material-symbols-outlined">drag_indicator</span>
</div>
<div class="flex-grow flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">warning</span>
<span class="font-body-md text-body-md text-on-surface font-semibold">Risks</span>
</div>
<div class="flex items-center gap-base">
<button class="material-symbols-outlined text-secondary hover:text-primary p-xs rounded-lg hover:bg-surface-container transition-colors" title="Rename">edit</button>
<button class="material-symbols-outlined text-secondary hover:text-error p-xs rounded-lg hover:bg-surface-container transition-colors" title="Delete">delete</button>
</div>
</div>
</div>
<!-- Add New Quick Section Button -->
<div class="mt-sm">
<button class="w-full py-md border-2 border-dashed border-outline-variant rounded-xl text-outline hover:border-primary hover:text-primary transition-all flex items-center justify-center gap-xs">
<span class="material-symbols-outlined">add_circle</span>
<span class="font-label-md text-label-md">New Proposal Module</span>
</button>
</div>
</div>
</main>
<!-- BottomNavBar from JSON -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<div class="flex gap-sm">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs font-label-md text-label-md hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150 rounded-xl">
<span class="material-symbols-outlined mr-xs">arrow_back</span>
        Back
      </button>
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs font-label-md text-label-md hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150 rounded-xl">
<span class="material-symbols-outlined mr-xs">close</span>
        Cancel
      </button>
</div>
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-sm py-xs font-label-md text-label-md hover:opacity-90 active:scale-95 duration-150">
      Approve Structure
      <span class="material-symbols-outlined ml-xs">arrow_forward</span>
</button>
</footer>
<!-- Mock interaction for drag and drop simulation -->
<script>
    document.querySelectorAll('.drag-handle').forEach(handle => {
      handle.addEventListener('mousedown', () => {
        handle.closest('.group').style.opacity = '0.7';
        handle.closest('.group').style.cursor = 'grabbing';
      });
      window.addEventListener('mouseup', () => {
        handle.closest('.group').style.opacity = '1';
        handle.closest('.group').style.cursor = 'default';
      });
    });
  </script>
</body></html>



<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Proposal Generation Progress | Proposal Copilot</title>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Google Fonts: Inter -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-fixed-dim": "#bec6e0",
                        "inverse-surface": "#2d3133",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-fixed-variant": "#574425",
                        "on-secondary-fixed-variant": "#38485d",
                        "surface-bright": "#f7f9fb",
                        "surface-container": "#eceef0",
                        "on-primary-fixed-variant": "#3f465c",
                        "on-secondary-container": "#54647a",
                        "on-tertiary-fixed": "#271901",
                        "tertiary-fixed-dim": "#dec29a",
                        "secondary-fixed": "#d3e4fe",
                        "tertiary": "#000000",
                        "primary-container": "#131b2e",
                        "surface-container-high": "#e6e8ea",
                        "on-secondary": "#ffffff",
                        "inverse-primary": "#bec6e0",
                        "on-error": "#ffffff",
                        "on-tertiary": "#ffffff",
                        "surface": "#f7f9fb",
                        "on-error-container": "#93000a",
                        "primary-fixed": "#dae2fd",
                        "tertiary-fixed": "#fcdeb5",
                        "secondary-container": "#d0e1fb",
                        "surface-dim": "#d8dadc",
                        "on-tertiary-container": "#98805d",
                        "secondary-fixed-dim": "#b7c8e1",
                        "surface-tint": "#565e74",
                        "outline-variant": "#c6c6cd",
                        "tertiary-container": "#271901",
                        "outline": "#76777d",
                        "on-primary-fixed": "#131b2e",
                        "on-secondary-fixed": "#0b1c30",
                        "error": "#ba1a1a",
                        "inverse-on-surface": "#eff1f3",
                        "on-primary-container": "#7c839b",
                        "on-primary": "#ffffff",
                        "primary": "#000000",
                        "on-surface": "#191c1e",
                        "secondary": "#505f76",
                        "surface-container-highest": "#e0e3e5",
                        "on-background": "#191c1e",
                        "on-surface-variant": "#45464d",
                        "error-container": "#ffdad6",
                        "surface-container-low": "#f2f4f6",
                        "background": "#f7f9fb",
                        "surface-variant": "#e0e3e5"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "md": "24px",
                        "xs": "8px",
                        "base": "4px",
                        "sm": "16px",
                        "xl": "80px",
                        "container-max": "1280px",
                        "lg": "48px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "headline-lg-mobile": ["Inter"],
                        "label-md": ["Inter"],
                        "label-sm": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "headline-lg-mobile": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        body { font-family: 'Inter', sans-serif; background-color: #f7f9fb; }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            display: inline-block;
            vertical-align: middle;
        }
        .progress-ring__circle {
            transition: stroke-dashoffset 0.35s;
            transform: rotate(-90deg);
            transform-origin: 50% 50%;
        }
        /* Tonal Layering for Depth */
        .glass-panel {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(8px);
            border: 1px solid #E2E8F0;
        }
        .timeline-line {
            background: repeating-linear-gradient(to bottom, #cbd5e1 0, #cbd5e1 4px, transparent 4px, transparent 8px);
        }
    </style>
</head>
<body class="bg-background text-on-surface min-h-screen flex flex-col">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">
            Proposal Copilot
        </div>
<div class="flex items-center gap-md">
<span class="material-symbols-outlined text-primary dark:text-inverse-primary cursor-pointer hover:bg-surface-container dark:hover:bg-surface-container-highest transition-colors p-2 rounded-full">
                account_circle
            </span>
</div>
</header>
<!-- Main Content -->
<main class="flex-grow pt-32 pb-xl px-md max-w-container-max mx-auto w-full">
<div class="grid grid-cols-1 lg:grid-cols-12 gap-lg">
<!-- Left: Large Circular Progress (The Focal Point) -->
<div class="lg:col-span-7 flex flex-col items-center justify-center space-y-md">
<div class="relative flex items-center justify-center p-lg bg-white rounded-xl shadow-sm border border-outline-variant w-full aspect-square max-w-[500px]">
<!-- Circular Progress SVG -->
<svg class="w-full h-full" viewBox="0 0 120 120">
<!-- Background Circle -->
<circle class="text-surface-container" cx="60" cy="60" fill="transparent" r="50" stroke="currentColor" stroke-width="8"></circle>
<!-- Progress Circle -->
<circle class="text-primary transition-all duration-1000 ease-out progress-ring__circle" cx="60" cy="60" fill="transparent" r="50" stroke="currentColor" stroke-dasharray="314.159" stroke-dashoffset="87.96" stroke-linecap="round" stroke-width="8"></circle>
</svg>
<!-- Text Overlay -->
<div class="absolute flex flex-col items-center text-center">
<span class="font-display-lg text-display-lg text-primary">72%</span>
<span class="font-label-md text-label-md text-secondary tracking-widest uppercase mt-xs">Complete</span>
</div>
</div>
<div class="text-center space-y-xs">
<h2 class="font-headline-md text-headline-md text-on-surface">Generating Executive Summary</h2>
<p class="font-body-md text-body-md text-on-surface-variant max-w-md mx-auto">
                        Synthesizing your project scope with the retrieved technical constraints to draft a high-impact introduction.
                    </p>
</div>
</div>
<!-- Right: Vertical Workflow Timeline -->
<div class="lg:col-span-5">
<div class="bg-white rounded-xl p-lg border border-outline-variant shadow-sm h-full">
<h3 class="font-headline-md text-headline-md mb-lg">Workflow Timeline</h3>
<div class="relative flex flex-col space-y-xl">
<!-- Progress Line -->
<div class="absolute left-4 top-2 bottom-2 w-0.5 timeline-line z-0"></div>
<!-- Step 1: Completed -->
<div class="relative flex items-start z-10">
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white mr-md">
<span class="material-symbols-outlined text-[18px]">check</span>
</div>
<div>
<h4 class="font-label-md text-label-md text-primary">Requirement Analysis</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant">RFP documents parsed and key mandates identified.</p>
</div>
</div>
<!-- Step 2: Completed -->
<div class="relative flex items-start z-10">
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white mr-md">
<span class="material-symbols-outlined text-[18px]">check</span>
</div>
<div>
<h4 class="font-label-md text-label-md text-primary">Context Retrieval</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant">Relevant technical case studies and pricing history fetched.</p>
</div>
</div>
<!-- Step 3: Completed -->
<div class="relative flex items-start z-10">
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white mr-md">
<span class="material-symbols-outlined text-[18px]">check</span>
</div>
<div>
<h4 class="font-label-md text-label-md text-primary">Structure Alignment</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant">Mapping proposal structure to client-mandated templates.</p>
</div>
</div>
<!-- Step 4: In Progress -->
<div class="relative flex items-start z-10">
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-white border-2 border-primary flex items-center justify-center text-primary mr-md">
<span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
</div>
<div>
<h4 class="font-label-md text-label-md text-primary">Section Generation</h4>
<p class="font-body-sm text-body-sm text-on-surface">Writing 'Executive Summary' and 'Technical Approach'.</p>
</div>
</div>
<!-- Step 5: Pending -->
<div class="relative flex items-start z-10">
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-surface-container border border-outline-variant flex items-center justify-center text-outline mr-md">
<span class="material-symbols-outlined text-[18px]">horizontal_rule</span>
</div>
<div>
<h4 class="font-label-md text-label-md text-on-surface-variant">Grounding Validation</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant">Verifying all AI claims against company knowledge base.</p>
</div>
</div>
<!-- Step 6: Pending -->
<div class="relative flex items-start z-10">
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-surface-container border border-outline-variant flex items-center justify-center text-outline mr-md">
<span class="material-symbols-outlined text-[18px]">lock</span>
</div>
<div>
<h4 class="font-label-md text-label-md text-on-surface-variant">Proposal Assembly</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant">Formatting final PDF and preparing for export.</p>
</div>
</div>
</div>
</div>
</div>
</div>
</main>
<!-- BottomNavBar -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
<!-- Continue is technically disabled or "Waiting" during generation, but shown per JSON -->
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-sm py-xs opacity-50 cursor-not-allowed">
<span class="font-label-md text-label-md mr-xs">Continue</span>
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</footer>
<!-- Subtle Background Element -->
<div class="fixed inset-0 -z-10 pointer-events-none overflow-hidden">
<div class="absolute -top-1/4 -right-1/4 w-[800px] h-[800px] bg-secondary-container opacity-20 blur-[120px] rounded-full"></div>
<div class="absolute -bottom-1/4 -left-1/4 w-[600px] h-[600px] bg-primary-fixed opacity-30 blur-[100px] rounded-full"></div>
</div>
<script>
        // Micro-interaction: Progress Ring animation logic (simulated)
        document.addEventListener('DOMContentLoaded', () => {
            const circle = document.querySelector('.progress-ring__circle');
            const radius = circle.r.baseVal.value;
            const circumference = radius * 2 * Math.PI;

            circle.style.strokeDasharray = `${circumference} ${circumference}`;
            
            function setProgress(percent) {
                const offset = circumference - (percent / 100 * circumference);
                circle.style.strokeDashoffset = offset;
            }

            // Set the initial progress from the prompt (72%)
            setTimeout(() => {
                setProgress(72);
            }, 500);
        });
    </script>
</body></html>


<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Proposal Copilot - Input Consolidation</title>
<!-- Google Fonts: Inter -->
<link href="https://fonts.googleapis.com" rel="preconnect">
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<!-- Material Symbols Outlined -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              "colors": {
                      "primary-fixed-dim": "#bec6e0",
                      "inverse-surface": "#2d3133",
                      "surface-container-lowest": "#ffffff",
                      "on-tertiary-fixed-variant": "#574425",
                      "on-secondary-fixed-variant": "#38485d",
                      "surface-bright": "#f7f9fb",
                      "surface-container": "#eceef0",
                      "on-primary-fixed-variant": "#3f465c",
                      "on-secondary-container": "#54647a",
                      "on-tertiary-fixed": "#271901",
                      "tertiary-fixed-dim": "#dec29a",
                      "secondary-fixed": "#d3e4fe",
                      "tertiary": "#000000",
                      "primary-container": "#131b2e",
                      "surface-container-high": "#e6e8ea",
                      "on-secondary": "#ffffff",
                      "inverse-primary": "#bec6e0",
                      "on-error": "#ffffff",
                      "on-tertiary": "#ffffff",
                      "surface": "#f7f9fb",
                      "on-error-container": "#93000a",
                      "primary-fixed": "#dae2fd",
                      "tertiary-fixed": "#fcdeb5",
                      "secondary-container": "#d0e1fb",
                      "surface-dim": "#d8dadc",
                      "on-tertiary-container": "#98805d",
                      "secondary-fixed-dim": "#b7c8e1",
                      "surface-tint": "#565e74",
                      "outline-variant": "#c6c6cd",
                      "tertiary-container": "#271901",
                      "outline": "#76777d",
                      "on-primary-fixed": "#131b2e",
                      "on-secondary-fixed": "#0b1c30",
                      "error": "#ba1a1a",
                      "inverse-on-surface": "#eff1f3",
                      "on-primary-container": "#7c839b",
                      "on-primary": "#ffffff",
                      "primary": "#000000",
                      "on-surface": "#191c1e",
                      "secondary": "#505f76",
                      "surface-container-highest": "#e0e3e5",
                      "on-background": "#191c1e",
                      "on-surface-variant": "#45464d",
                      "error-container": "#ffdad6",
                      "surface-container-low": "#f2f4f6",
                      "background": "#f7f9fb",
                      "surface-variant": "#e0e3e5"
              },
              "borderRadius": {
                      "DEFAULT": "0.125rem",
                      "lg": "0.25rem",
                      "xl": "0.5rem",
                      "full": "0.75rem"
              },
              "spacing": {
                      "gutter": "24px",
                      "md": "24px",
                      "xs": "8px",
                      "base": "4px",
                      "sm": "16px",
                      "xl": "80px",
                      "container-max": "1280px",
                      "lg": "48px"
              },
              "fontFamily": {
                      "headline-lg": ["Inter"],
                      "headline-md": ["Inter"],
                      "headline-lg-mobile": ["Inter"],
                      "label-md": ["Inter"],
                      "label-sm": ["Inter"],
                      "body-md": ["Inter"],
                      "body-lg": ["Inter"],
                      "display-lg": ["Inter"],
                      "body-sm": ["Inter"]
              },
              "fontSize": {
                      "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                      "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                      "headline-lg-mobile": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                      "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                      "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                      "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                      "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                      "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                      "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
              }
            },
          },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            display: inline-block;
            vertical-align: middle;
        }
        body {
            background-color: #f7f9fb;
            font-family: 'Inter', sans-serif;
            color: #191c1e;
        }
        .summary-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            transition: box-shadow 0.2s ease;
        }
        .summary-card:hover {
            box-shadow: 0px 4px 20px rgba(15, 23, 42, 0.05);
        }
        .source-badge {
            background-color: #f1f5f9;
            color: #475569;
            border-radius: 2px;
            padding: 2px 8px;
            font-size: 12px;
            font-weight: 600;
        }
        .missing-info-container {
            background: #fff5f5;
            border-left: 4px solid #ba1a1a;
        }
    </style>
</head>
<body class="min-h-screen pb-32">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface border-b border-outline-variant">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface">Proposal Copilot</span>
</div>
<div class="flex items-center gap-md">
<nav class="hidden md:flex gap-md">
<a class="text-on-surface-variant hover:bg-surface-container transition-colors px-xs py-base font-label-md text-label-md" href="#">Dashboard</a>
<a class="text-primary font-bold border-b-2 border-primary px-xs py-base font-label-md text-label-md" href="#">Consolidation</a>
<a class="text-on-surface-variant hover:bg-surface-container transition-colors px-xs py-base font-label-md text-label-md" href="#">Library</a>
</nav>
<button class="material-symbols-outlined text-primary hover:bg-surface-container transition-colors p-xs rounded-full">account_circle</button>
</div>
</header>
<main class="pt-24 max-w-container-max mx-auto px-gutter">
<div class="mb-lg">
<h1 class="font-headline-lg text-headline-lg text-primary">Input Consolidation</h1>
<p class="font-body-md text-body-md text-secondary mt-xs">Reviewing and synthesizing information from all identified sources to build your proposal foundation.</p>
</div>
<!-- Two-Column Layout -->
<div class="grid grid-cols-1 lg:grid-cols-3 gap-lg">
<!-- Left Side: Information Sources -->
<div class="lg:col-span-1 space-y-sm">
<h2 class="font-label-md text-label-md text-outline uppercase tracking-wider">Information Sources</h2>
<div class="space-y-xs">
<!-- Source Item -->
<div class="summary-card p-sm flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary">database</span>
<span class="font-label-md text-label-md">Metadata</span>
</div>
<span class="source-badge">VERIFIED</span>
</div>
<!-- Source Item -->
<div class="summary-card p-sm flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary">quiz</span>
<span class="font-label-md text-label-md">Questionnaire</span>
</div>
<span class="source-badge">80% COMPLETE</span>
</div>
<!-- Source Item -->
<div class="summary-card p-sm flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary">terminal</span>
<span class="font-label-md text-label-md">Prompt Inputs</span>
</div>
<span class="source-badge">ACTIVE</span>
</div>
<!-- Source Item -->
<div class="summary-card p-sm flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary">record_voice_over</span>
<span class="font-label-md text-label-md">Meeting Transcript</span>
</div>
<span class="source-badge">PROCESSED</span>
</div>
<!-- Source Item -->
<div class="summary-card p-sm flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary">description</span>
<span class="font-label-md text-label-md">MOM</span>
</div>
<span class="source-badge">UPLOADED</span>
</div>
<!-- Source Item -->
<div class="summary-card p-sm flex items-center justify-between">
<div class="flex items-center gap-sm">
<span class="material-symbols-outlined text-secondary">contract</span>
<span class="font-label-md text-label-md">RFP</span>
</div>
<span class="source-badge">ANALYZED</span>
</div>
</div>
<div class="mt-lg p-sm bg-surface-container-low rounded-lg border border-outline-variant">
<div class="flex items-center gap-xs text-secondary mb-xs">
<span class="material-symbols-outlined text-sm">auto_awesome</span>
<span class="font-label-sm text-label-sm">AI INSIGHT</span>
</div>
<p class="font-body-sm text-body-sm italic">"High correlation found between Meeting Transcripts and RFP requirements regarding 'Cloud Security' modules."</p>
</div>
</div>
<!-- Right Side: Consolidated Information Summary -->
<div class="lg:col-span-2 space-y-sm">
<h2 class="font-label-md text-label-md text-outline uppercase tracking-wider">Consolidated Information</h2>
<div class="summary-card p-lg grid grid-cols-1 md:grid-cols-2 gap-md">
<!-- Detail Section -->
<div class="space-y-base">
<label class="font-label-sm text-label-sm text-secondary uppercase">Client Name</label>
<p class="font-body-md text-body-md font-semibold">Global Dynamics Int.</p>
</div>
<!-- Detail Section -->
<div class="space-y-base">
<label class="font-label-sm text-label-sm text-secondary uppercase">Timeline</label>
<p class="font-body-md text-body-md font-semibold">Q3 2024 (Phase 1 Rollout)</p>
</div>
<!-- Detail Section -->
<div class="space-y-base col-span-1 md:col-span-2">
<label class="font-label-sm text-label-sm text-secondary uppercase">Business Objectives</label>
<ul class="list-disc list-inside font-body-md text-body-md space-y-xs">
<li>Modernize legacy procurement workflows by 40%</li>
<li>Enable real-time AI analytics for vendor selection</li>
<li>Reduce operational overhead by centralizing proposal lifecycles</li>
</ul>
</div>
<!-- Detail Section -->
<div class="space-y-base">
<label class="font-label-sm text-label-sm text-secondary uppercase">Stakeholders</label>
<div class="flex flex-wrap gap-xs">
<span class="px-xs py-base bg-surface-container-high rounded-lg font-label-sm text-label-sm">Sarah Chen (CTO)</span>
<span class="px-xs py-base bg-surface-container-high rounded-lg font-label-sm text-label-sm">Mark Vane (Procurement)</span>
</div>
</div>
<!-- Detail Section -->
<div class="space-y-base">
<label class="font-label-sm text-label-sm text-secondary uppercase">Budget</label>
<p class="font-body-md text-body-md font-semibold">$450,000 - $600,000 USD</p>
</div>
<!-- Detail Section -->
<div class="space-y-base col-span-1 md:col-span-2">
<label class="font-label-sm text-label-sm text-secondary uppercase">Core Requirements</label>
<div class="flex flex-wrap gap-xs">
<span class="px-xs py-base border border-outline-variant rounded font-label-sm text-label-sm">SSO Integration</span>
<span class="px-xs py-base border border-outline-variant rounded font-label-sm text-label-sm">SOC2 Compliance</span>
<span class="px-xs py-base border border-outline-variant rounded font-label-sm text-label-sm">24/7 Support</span>
<span class="px-xs py-base border border-outline-variant rounded font-label-sm text-label-sm">Custom API Access</span>
</div>
</div>
</div>
<!-- Below: Missing Information section -->
<div class="mt-lg">
<h2 class="font-label-md text-label-md text-error uppercase tracking-wider mb-sm">Missing Information</h2>
<div class="missing-info-container p-md rounded-xl space-y-md">
<div class="flex items-start gap-sm">
<span class="material-symbols-outlined text-error mt-1">warning</span>
<div class="flex-1">
<h3 class="font-label-md text-label-md text-error">Unanswered Critical Questions</h3>
<div class="mt-sm space-y-sm">
<div class="p-sm bg-white rounded border border-red-100 flex justify-between items-center group cursor-pointer hover:border-red-300 transition-all">
<div>
<p class="font-label-sm text-label-sm text-secondary">Project KPI</p>
<p class="font-body-md text-body-md">What are the specific Success Metrics for the first 90 days?</p>
</div>
<span class="material-symbols-outlined text-outline group-hover:text-primary">edit</span>
</div>
<div class="p-sm bg-white rounded border border-red-100 flex justify-between items-center group cursor-pointer hover:border-red-300 transition-all">
<div>
<p class="font-label-sm text-label-sm text-secondary">Operations</p>
<p class="font-body-md text-body-md">Has the preferred Support Model (Follow-the-sun vs. Local) been finalized?</p>
</div>
<span class="material-symbols-outlined text-outline group-hover:text-primary">edit</span>
</div>
<div class="p-sm bg-white rounded border border-red-100 flex justify-between items-center group cursor-pointer hover:border-red-300 transition-all">
<div>
<p class="font-label-sm text-label-sm text-secondary">Infrastructure</p>
<p class="font-body-md text-body-md">Are there any specific Deployment Constraints regarding regional data residency?</p>
</div>
<span class="material-symbols-outlined text-outline group-hover:text-primary">edit</span>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</main>
<!-- BottomNavBar -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest border-t border-outline-variant shadow-md">
<div class="flex gap-sm">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
</div>
<button class="flex items-center justify-center bg-primary text-on-primary rounded-xl px-sm py-xs hover:opacity-80 transition-all active:scale-95 duration-150">
<span class="font-label-md text-label-md">Continue</span>
<span class="material-symbols-outlined ml-xs">arrow_forward</span>
</button>
</footer>
<script>
        // Simple interactivity for the 'Missing Information' items
        document.querySelectorAll('.missing-info-container > div > div > div > div').forEach(item => {
            item.addEventListener('click', () => {
                const label = item.querySelector('.font-label-sm').innerText;
                console.log(`Open editor for: ${label}`);
                item.classList.toggle('ring-2');
                item.classList.toggle('ring-primary');
            });
        });
    </script>
</body></html>




<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Generation Setup - Proposal Copilot</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          "colors": {
            "primary-fixed-dim": "#bec6e0",
            "inverse-surface": "#2d3133",
            "surface-container-lowest": "#ffffff",
            "on-tertiary-fixed-variant": "#574425",
            "on-secondary-fixed-variant": "#38485d",
            "surface-bright": "#f7f9fb",
            "surface-container": "#eceef0",
            "on-primary-fixed-variant": "#3f465c",
            "on-secondary-container": "#54647a",
            "on-tertiary-fixed": "#271901",
            "tertiary-fixed-dim": "#dec29a",
            "secondary-fixed": "#d3e4fe",
            "tertiary": "#000000",
            "primary-container": "#131b2e",
            "surface-container-high": "#e6e8ea",
            "on-secondary": "#ffffff",
            "inverse-primary": "#bec6e0",
            "on-error": "#ffffff",
            "on-tertiary": "#ffffff",
            "surface": "#f7f9fb",
            "on-error-container": "#93000a",
            "primary-fixed": "#dae2fd",
            "tertiary-fixed": "#fcdeb5",
            "secondary-container": "#d0e1fb",
            "surface-dim": "#d8dadc",
            "on-tertiary-container": "#98805d",
            "secondary-fixed-dim": "#b7c8e1",
            "surface-tint": "#565e74",
            "outline-variant": "#c6c6cd",
            "tertiary-container": "#271901",
            "outline": "#76777d",
            "on-primary-fixed": "#131b2e",
            "on-secondary-fixed": "#0b1c30",
            "error": "#ba1a1a",
            "inverse-on-surface": "#eff1f3",
            "on-primary-container": "#7c839b",
            "on-primary": "#ffffff",
            "primary": "#000000",
            "on-surface": "#191c1e",
            "secondary": "#505f76",
            "surface-container-highest": "#e0e3e5",
            "on-background": "#191c1e",
            "on-surface-variant": "#45464d",
            "error-container": "#ffdad6",
            "surface-container-low": "#f2f4f6",
            "background": "#f7f9fb",
            "surface-variant": "#e0e3e5"
          },
          "borderRadius": {
            "DEFAULT": "0.125rem",
            "lg": "0.25rem",
            "xl": "0.5rem",
            "full": "0.75rem"
          },
          "spacing": {
            "gutter": "24px",
            "md": "24px",
            "xs": "8px",
            "base": "4px",
            "sm": "16px",
            "xl": "80px",
            "container-max": "1280px",
            "lg": "48px"
          },
          "fontFamily": {
            "headline-lg": ["Inter"],
            "headline-md": ["Inter"],
            "label-md": ["Inter"],
            "label-sm": ["Inter"],
            "body-md": ["Inter"],
            "body-lg": ["Inter"],
            "display-lg": ["Inter"],
            "body-sm": ["Inter"]
          },
          "fontSize": {
            "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
            "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
            "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
            "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
            "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
            "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
            "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
            "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
          }
        },
      },
    }
  </script>
<style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #f7f9fb;
    }
    .material-symbols-outlined {
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }
    .check-circle-anim {
      animation: checkFade 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes checkFade {
      from { opacity: 0; transform: scale(0.8); }
      to { opacity: 1; transform: scale(1); }
    }
    .glass-effect {
      background: rgba(255, 255, 255, 0.8);
      backdrop-filter: blur(8px);
    }
  </style>
</head>
<body class="bg-background text-on-surface min-h-screen flex flex-col">
<!-- TopAppBar Component -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface border-b border-outline-variant">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface">Proposal Copilot</span>
</div>
<nav class="hidden md:flex items-center gap-md">
<a class="font-label-md text-label-md text-on-surface-variant hover:bg-surface-container transition-colors px-sm py-xs" href="#">Projects</a>
<a class="font-label-md text-label-md text-on-surface-variant hover:bg-surface-container transition-colors px-sm py-xs" href="#">Templates</a>
<a class="font-label-md text-label-md text-primary font-bold border-b-2 border-primary px-sm py-xs" href="#">New Proposal</a>
</nav>
<div class="flex items-center">
<button class="material-symbols-outlined text-primary hover:bg-surface-container transition-colors p-xs rounded-full">account_circle</button>
</div>
</header>
<main class="flex-grow pt-32 pb-xl px-md flex items-center justify-center relative overflow-hidden">
<!-- Atmospheric Background Decoration -->
<div class="absolute top-1/4 -left-20 w-96 h-96 bg-primary-fixed-dim/20 rounded-full blur-[100px] pointer-events-none"></div>
<div class="absolute bottom-1/4 -right-20 w-96 h-96 bg-secondary-container/30 rounded-full blur-[100px] pointer-events-none"></div>
<div class="w-full max-w-2xl z-10">
<!-- Centered Summary Card -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl shadow-[0px_4px_20px_rgba(15,23,42,0.05)] p-lg space-y-lg">
<!-- Header Section -->
<div class="text-center space-y-xs">
<h1 class="font-headline-lg text-headline-lg text-on-surface">Final Readiness Review</h1>
<p class="font-body-md text-body-md text-on-surface-variant">Your configuration is complete. Review the status below and customize research options before generation.</p>
</div>
<!-- Readiness Status Grid -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-sm">
<div class="flex flex-col items-center p-sm bg-surface-container-low rounded-lg border border-outline-variant/30">
<span class="material-symbols-outlined text-[#059669] mb-xs check-circle-anim" style="font-variation-settings: 'FILL' 1;">check_circle</span>
<span class="font-label-md text-label-md text-center">Proposal Structure Approved</span>
</div>
<div class="flex flex-col items-center p-sm bg-surface-container-low rounded-lg border border-outline-variant/30">
<span class="material-symbols-outlined text-[#059669] mb-xs check-circle-anim" style="font-variation-settings: 'FILL' 1;">check_circle</span>
<span class="font-label-md text-label-md text-center">Input Collection Completed</span>
</div>
<div class="flex flex-col items-center p-sm bg-primary/5 border border-primary/20 rounded-lg">
<span class="font-label-sm text-label-sm text-primary uppercase tracking-widest mb-xs">Readiness Status</span>
<span class="font-headline-md text-headline-md text-primary font-bold">Ready</span>
</div>
</div>
<!-- Research Options Section -->
<div class="space-y-sm">
<h2 class="font-label-md text-label-md text-on-surface-variant flex items-center gap-xs">
<span class="material-symbols-outlined text-[20px]">travel_explore</span>
            Web Research Options
          </h2>
<div class="grid grid-cols-1 md:grid-cols-2 gap-md bg-surface-bright p-md rounded-xl border border-outline-variant">
<label class="flex items-start gap-sm cursor-pointer group">
<div class="relative flex items-center mt-0.5">
<input checked="" class="peer h-5 w-5 rounded border-outline text-primary focus:ring-primary transition-all" type="checkbox">
</div>
<div class="flex flex-col">
<span class="font-body-md text-body-md font-semibold text-on-surface group-hover:text-primary transition-colors">Enable Client Research</span>
<span class="font-body-sm text-body-sm text-on-surface-variant">Scan client website, news, and recent press releases.</span>
</div>
</label>
<label class="flex items-start gap-sm cursor-pointer group">
<div class="relative flex items-center mt-0.5">
<input checked="" class="peer h-5 w-5 rounded border-outline text-primary focus:ring-primary transition-all" type="checkbox">
</div>
<div class="flex flex-col">
<span class="font-body-md text-body-md font-semibold text-on-surface group-hover:text-primary transition-colors">Enable Industry Research</span>
<span class="font-body-sm text-body-sm text-on-surface-variant">Analyze market trends and competitor benchmarks.</span>
</div>
</label>
<label class="flex items-start gap-sm cursor-pointer group">
<div class="relative flex items-center mt-0.5">
<input class="peer h-5 w-5 rounded border-outline text-primary focus:ring-primary transition-all" type="checkbox">
</div>
<div class="flex flex-col">
<span class="font-body-md text-body-md font-semibold text-on-surface group-hover:text-primary transition-colors">Enable Architecture Research</span>
<span class="font-body-sm text-body-sm text-on-surface-variant">Lookup technical documentation for specified stack.</span>
</div>
</label>
<label class="flex items-start gap-sm cursor-pointer group">
<div class="relative flex items-center mt-0.5">
<input checked="" class="peer h-5 w-5 rounded border-outline text-primary focus:ring-primary transition-all" type="checkbox">
</div>
<div class="flex flex-col">
<span class="font-body-md text-body-md font-semibold text-on-surface group-hover:text-primary transition-colors">Enable Timeline Suggestions</span>
<span class="font-body-sm text-body-sm text-on-surface-variant">Use AI to project realistic milestone dates.</span>
</div>
</label>
</div>
</div>
<!-- Action Section -->
<div class="pt-md flex flex-col items-center">
<button class="w-full py-sm bg-primary text-on-primary rounded-xl font-label-md text-label-md hover:opacity-90 active:scale-[0.98] transition-all flex items-center justify-center gap-sm group" id="generateBtn">
<span id="btnText">Generate Proposal</span>
<span class="material-symbols-outlined group-hover:translate-x-1 transition-transform">auto_awesome</span>
</button>
<p class="mt-sm font-label-sm text-label-sm text-on-surface-variant">Estimated generation time: 45-60 seconds</p>
</div>
</div>
</div>
</main>
<!-- BottomNavBar Component (Transactional Step) -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest border-t border-outline-variant shadow-md">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<div class="flex gap-md">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
<button class="flex items-center justify-center bg-primary text-on-primary rounded-xl px-sm py-xs opacity-50 cursor-not-allowed">
<span class="font-label-md text-label-md">Continue</span>
<span class="material-symbols-outlined ml-xs">arrow_forward</span>
</button>
</div>
</footer>
<script>
    const generateBtn = document.getElementById('generateBtn');
    const btnText = document.getElementById('btnText');
    
    generateBtn.addEventListener('click', () => {
      const originalContent = generateBtn.innerHTML;
      generateBtn.disabled = true;
      generateBtn.classList.add('opacity-80', 'cursor-not-allowed');
      
      btnText.textContent = "Initializing AI Engine...";
      
      // Simulate loading state
      let progress = 0;
      const interval = setInterval(() => {
        progress += 10;
        if (progress > 100) {
          clearInterval(interval);
          btnText.textContent = "Crafting Content...";
        }
      }, 300);

      // Micro-interaction: Subtle pulse while working
      generateBtn.classList.add('animate-pulse');
    });

    // Ripple effect for the primary button
    generateBtn.addEventListener('mousedown', function(e) {
      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const ripple = document.createElement('span');
      ripple.style.position = 'absolute';
      ripple.style.left = x + 'px';
      ripple.style.top = y + 'px';
      ripple.style.width = '0';
      ripple.style.height = '0';
      ripple.style.background = 'rgba(255, 255, 255, 0.2)';
      ripple.style.borderRadius = '50%';
      ripple.style.transform = 'translate(-50%, -50%)';
      ripple.style.transition = 'width 0.4s ease, height 0.4s ease, opacity 0.4s ease';
      
      this.appendChild(ripple);
      
      setTimeout(() => {
        ripple.style.width = '400px';
        ripple.style.height = '400px';
        ripple.style.opacity = '0';
      }, 0);
      
      setTimeout(() => ripple.remove(), 400);
    });
  </script>
</body></html>


<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Section Generation Tracking - Proposal Copilot</title>
<!-- Google Fonts: Inter -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<!-- Material Symbols Outlined -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "primary-fixed-dim": "#bec6e0",
                    "inverse-surface": "#2d3133",
                    "surface-container-lowest": "#ffffff",
                    "on-tertiary-fixed-variant": "#574425",
                    "on-secondary-fixed-variant": "#38485d",
                    "surface-bright": "#f7f9fb",
                    "surface-container": "#eceef0",
                    "on-primary-fixed-variant": "#3f465c",
                    "on-secondary-container": "#54647a",
                    "on-tertiary-fixed": "#271901",
                    "tertiary-fixed-dim": "#dec29a",
                    "secondary-fixed": "#d3e4fe",
                    "tertiary": "#000000",
                    "primary-container": "#131b2e",
                    "surface-container-high": "#e6e8ea",
                    "on-secondary": "#ffffff",
                    "inverse-primary": "#bec6e0",
                    "on-error": "#ffffff",
                    "on-tertiary": "#ffffff",
                    "surface": "#f7f9fb",
                    "on-error-container": "#93000a",
                    "primary-fixed": "#dae2fd",
                    "tertiary-fixed": "#fcdeb5",
                    "secondary-container": "#d0e1fb",
                    "surface-dim": "#d8dadc",
                    "on-tertiary-container": "#98805d",
                    "secondary-fixed-dim": "#b7c8e1",
                    "surface-tint": "#565e74",
                    "outline-variant": "#c6c6cd",
                    "tertiary-container": "#271901",
                    "outline": "#76777d",
                    "on-primary-fixed": "#131b2e",
                    "on-secondary-fixed": "#0b1c30",
                    "error": "#ba1a1a",
                    "inverse-on-surface": "#eff1f3",
                    "on-primary-container": "#7c839b",
                    "on-primary": "#ffffff",
                    "primary": "#000000",
                    "on-surface": "#191c1e",
                    "secondary": "#505f76",
                    "surface-container-highest": "#e0e3e5",
                    "on-background": "#191c1e",
                    "on-surface-variant": "#45464d",
                    "error-container": "#ffdad6",
                    "surface-container-low": "#f2f4f6",
                    "background": "#f7f9fb",
                    "surface-variant": "#e0e3e5"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "spacing": {
                    "gutter": "24px",
                    "md": "24px",
                    "xs": "8px",
                    "base": "4px",
                    "sm": "16px",
                    "xl": "80px",
                    "container-max": "1280px",
                    "lg": "48px"
            },
            "fontFamily": {
                    "headline-lg": ["Inter"],
                    "headline-md": ["Inter"],
                    "headline-lg-mobile": ["Inter"],
                    "label-md": ["Inter"],
                    "label-sm": ["Inter"],
                    "body-md": ["Inter"],
                    "body-lg": ["Inter"],
                    "display-lg": ["Inter"],
                    "body-sm": ["Inter"]
            },
            "fontSize": {
                    "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                    "headline-lg-mobile": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                    "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                    "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                    "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                    "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                    "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        body { font-family: 'Inter', sans-serif; }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .progress-bar-shine {
            position: relative;
            overflow: hidden;
        }
        .progress-bar-shine::after {
            content: "";
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            animation: shine 2s infinite;
        }
        @keyframes shine {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
    </style>
</head>
<body class="bg-surface text-on-surface min-h-screen pb-xl">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">Proposal Copilot</span>
</div>
<nav class="hidden md:flex items-center gap-lg">
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container transition-colors px-sm py-xs rounded" href="#">Dashboard</a>
<a class="text-primary dark:text-inverse-primary font-bold border-b-2 border-primary font-label-md text-label-md px-sm py-xs" href="#">Generation Tracking</a>
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container transition-colors px-sm py-xs rounded" href="#">Library</a>
</nav>
<div class="flex items-center gap-md">
<button class="material-symbols-outlined text-primary dark:text-inverse-primary hover:bg-surface-container transition-colors p-xs rounded-full">account_circle</button>
</div>
</header>
<main class="pt-32 px-md md:px-lg max-w-container-max mx-auto">
<!-- Header Section -->
<div class="mb-lg">
<h1 class="font-headline-lg text-headline-lg mb-xs">Section Generation Tracking</h1>
<p class="font-body-md text-body-md text-secondary">Real-time status of your Enterprise RFP response components.</p>
</div>
<!-- Bento Grid of Section Cards -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-md">
<!-- Card 1: Executive Summary (Completed) -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col justify-between hover:shadow-md transition-shadow group">
<div>
<div class="flex justify-between items-start mb-sm">
<span class="material-symbols-outlined text-secondary" style="font-variation-settings: 'FILL' 1;">description</span>
<span class="bg-secondary-container text-on-secondary-container px-sm py-base text-label-sm font-label-sm rounded-full">Completed</span>
</div>
<h3 class="font-headline-md text-headline-md mb-xs">Executive Summary</h3>
<p class="font-body-sm text-body-sm text-secondary mb-md">High-level synthesis of value proposition and strategic alignment.</p>
</div>
<div class="space-y-md">
<div class="w-full bg-surface-container-high h-1.5 rounded-full overflow-hidden">
<div class="bg-primary h-full w-full"></div>
</div>
<button class="w-full h-[44px] bg-primary text-on-primary font-label-md text-label-md rounded hover:opacity-80 transition-opacity flex items-center justify-center gap-xs">
                        View Section
                        <span class="material-symbols-outlined text-[18px]">open_in_new</span>
</button>
</div>
</div>
<!-- Card 2: Business Context (Generating 45%) -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col justify-between hover:shadow-md transition-shadow border-primary/20">
<div>
<div class="flex justify-between items-start mb-sm">
<span class="material-symbols-outlined text-primary animate-pulse">sync</span>
<span class="bg-primary-fixed text-on-primary-fixed px-sm py-base text-label-sm font-label-sm rounded-full">Generating 45%</span>
</div>
<h3 class="font-headline-md text-headline-md mb-xs">Business Context</h3>
<p class="font-body-sm text-body-sm text-secondary mb-md">Analyzing organizational history and market positioning data.</p>
</div>
<div class="space-y-md">
<div class="w-full bg-surface-container-high h-1.5 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[45%] progress-bar-shine"></div>
</div>
<button class="w-full h-[44px] border-2 border-primary text-primary font-label-md text-label-md rounded hover:bg-surface-container transition-colors flex items-center justify-center gap-xs">
                        View Section
                        <span class="material-symbols-outlined text-[18px]">visibility</span>
</button>
</div>
</div>
<!-- Card 3: Technical Architecture (Retrieving Context) -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col justify-between hover:shadow-md transition-shadow">
<div>
<div class="flex justify-between items-start mb-sm">
<span class="material-symbols-outlined text-secondary">database</span>
<span class="bg-tertiary-fixed text-on-tertiary-fixed px-sm py-base text-label-sm font-label-sm rounded-full">Retrieving Context</span>
</div>
<h3 class="font-headline-md text-headline-md mb-xs">Technical Architecture</h3>
<p class="font-body-sm text-body-sm text-secondary mb-md">Scanning internal knowledge base for infrastructure specifications.</p>
</div>
<div class="space-y-md">
<div class="w-full bg-surface-container-high h-1.5 rounded-full overflow-hidden flex gap-1">
<div class="bg-outline h-full w-4 animate-bounce"></div>
<div class="bg-outline h-full w-4 animate-bounce [animation-delay:0.2s]"></div>
<div class="bg-outline h-full w-4 animate-bounce [animation-delay:0.4s]"></div>
</div>
<button class="w-full h-[44px] border-2 border-primary text-primary font-label-md text-label-md rounded hover:bg-surface-container transition-colors flex items-center justify-center gap-xs">
                        View Section
                        <span class="material-symbols-outlined text-[18px]">visibility</span>
</button>
</div>
</div>
<!-- Card 4: Implementation Plan (Waiting) -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col justify-between opacity-70">
<div>
<div class="flex justify-between items-start mb-sm">
<span class="material-symbols-outlined text-outline">schedule</span>
<span class="bg-surface-container-high text-on-surface-variant px-sm py-base text-label-sm font-label-sm rounded-full">Waiting</span>
</div>
<h3 class="font-headline-md text-headline-md mb-xs">Implementation Plan</h3>
<p class="font-body-sm text-body-sm text-secondary mb-md">Timeline and resource allocation strategy (Queued).</p>
</div>
<div class="space-y-md">
<div class="w-full bg-surface-container-high h-1.5 rounded-full overflow-hidden">
<div class="bg-outline h-full w-0"></div>
</div>
<button class="w-full h-[44px] border-2 border-outline-variant text-outline font-label-md text-label-md rounded cursor-not-allowed flex items-center justify-center gap-xs" disabled="">
                        View Section
                    </button>
</div>
</div>
<!-- Card 5: Pricing (Waiting) -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col justify-between opacity-70">
<div>
<div class="flex justify-between items-start mb-sm">
<span class="material-symbols-outlined text-outline">payments</span>
<span class="bg-surface-container-high text-on-surface-variant px-sm py-base text-label-sm font-label-sm rounded-full">Waiting</span>
</div>
<h3 class="font-headline-md text-headline-md mb-xs">Pricing</h3>
<p class="font-body-sm text-body-sm text-secondary mb-md">Dynamic commercial modelling and fee structure breakdown.</p>
</div>
<div class="space-y-md">
<div class="w-full bg-surface-container-high h-1.5 rounded-full overflow-hidden">
<div class="bg-outline h-full w-0"></div>
</div>
<button class="w-full h-[44px] border-2 border-outline-variant text-outline font-label-md text-label-md rounded cursor-not-allowed flex items-center justify-center gap-xs" disabled="">
                        View Section
                    </button>
</div>
</div>
<!-- Empty State / Add New Section -->
<div class="border-2 border-dashed border-outline-variant rounded-xl p-md flex flex-col items-center justify-center text-center hover:border-primary transition-colors cursor-pointer min-h-[280px]">
<span class="material-symbols-outlined text-outline-variant text-[48px] mb-sm group-hover:text-primary">add_circle</span>
<p class="font-label-md text-label-md text-secondary">Add Custom Section</p>
<p class="font-body-sm text-body-sm text-outline mt-xs">Define a specific area for the Copilot to focus on.</p>
</div>
</div>
<!-- Quick Summary Bar (Bottom Floating) -->
<div class="fixed bottom-lg left-1/2 -translate-x-1/2 bg-inverse-surface text-inverse-on-surface rounded-full px-lg py-md flex items-center gap-lg shadow-xl z-40 max-w-lg w-full">
<div class="flex items-center gap-xs">
<span class="material-symbols-outlined text-primary-fixed-dim" style="font-variation-settings: 'FILL' 1;">check_circle</span>
<span class="font-label-md text-label-md">1 Completed</span>
</div>
<div class="flex items-center gap-xs border-x border-outline/30 px-lg">
<span class="material-symbols-outlined text-primary-fixed animate-spin">refresh</span>
<span class="font-label-md text-label-md">2 In Progress</span>
</div>
<div class="flex items-center gap-xs">
<span class="material-symbols-outlined text-outline-variant">pause_circle</span>
<span class="font-label-md text-label-md">2 Queued</span>
</div>
</div>
</main>
<!-- BottomNavBar (Mobile Only) -->
<nav class="md:hidden fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high transition-all active:scale-95 duration-150 flex-col gap-1">
<span class="material-symbols-outlined" data-icon="arrow_back">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high transition-all active:scale-95 duration-150 flex-col gap-1">
<span class="material-symbols-outlined" data-icon="close">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-sm py-xs hover:bg-surface-container-high transition-all active:scale-95 duration-150 flex-col gap-1">
<span class="material-symbols-outlined" data-icon="arrow_forward">arrow_forward</span>
<span class="font-label-md text-label-md">Continue</span>
</button>
</nav>
<!-- Atmospheric Micro-Interaction Script -->
<script>
        document.querySelectorAll('.group').forEach(card => {
            card.addEventListener('mouseenter', () => {
                const icon = card.querySelector('.material-symbols-outlined');
                if (icon) icon.style.transform = 'scale(1.1)';
            });
            card.addEventListener('mouseleave', () => {
                const icon = card.querySelector('.material-symbols-outlined');
                if (icon) icon.style.transform = 'scale(1)';
            });
        });

        // Simulate progress update for Business Context
        let progress = 45;
        const progressBar = document.querySelector('.bg-primary.h-full.w-\\[45\\%\\]');
        const progressLabel = document.querySelector('.bg-primary-fixed.text-on-primary-fixed');

        setInterval(() => {
            if (progress < 99) {
                progress += Math.random() * 0.5;
                if (progressBar) progressBar.style.width = `${progress}%`;
                if (progressLabel) progressLabel.innerText = `Generating ${Math.floor(progress)}%`;
            }
        }, 3000);
    </script>
</body></html>



<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Generated Section Review - Proposal Copilot</title>
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Google Fonts: Inter -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Theme Config -->
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-fixed-dim": "#bec6e0",
                        "inverse-surface": "#2d3133",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-fixed-variant": "#574425",
                        "on-secondary-fixed-variant": "#38485d",
                        "surface-bright": "#f7f9fb",
                        "surface-container": "#eceef0",
                        "on-primary-fixed-variant": "#3f465c",
                        "on-secondary-container": "#54647a",
                        "on-tertiary-fixed": "#271901",
                        "tertiary-fixed-dim": "#dec29a",
                        "secondary-fixed": "#d3e4fe",
                        "tertiary": "#000000",
                        "primary-container": "#131b2e",
                        "surface-container-high": "#e6e8ea",
                        "on-secondary": "#ffffff",
                        "inverse-primary": "#bec6e0",
                        "on-error": "#ffffff",
                        "on-tertiary": "#ffffff",
                        "surface": "#f7f9fb",
                        "on-error-container": "#93000a",
                        "primary-fixed": "#dae2fd",
                        "tertiary-fixed": "#fcdeb5",
                        "secondary-container": "#d0e1fb",
                        "surface-dim": "#d8dadc",
                        "on-tertiary-container": "#98805d",
                        "secondary-fixed-dim": "#b7c8e1",
                        "surface-tint": "#565e74",
                        "outline-variant": "#c6c6cd",
                        "tertiary-container": "#271901",
                        "outline": "#76777d",
                        "on-primary-fixed": "#131b2e",
                        "on-secondary-fixed": "#0b1c30",
                        "error": "#ba1a1a",
                        "inverse-on-surface": "#eff1f3",
                        "on-primary-container": "#7c839b",
                        "on-primary": "#ffffff",
                        "primary": "#000000",
                        "on-surface": "#191c1e",
                        "secondary": "#505f76",
                        "surface-container-highest": "#e0e3e5",
                        "on-background": "#191c1e",
                        "on-surface-variant": "#45464d",
                        "error-container": "#ffdad6",
                        "surface-container-low": "#f2f4f6",
                        "background": "#f7f9fb",
                        "surface-variant": "#e0e3e5"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "md": "24px",
                        "xs": "8px",
                        "base": "4px",
                        "sm": "16px",
                        "xl": "80px",
                        "container-max": "1280px",
                        "lg": "48px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "label-md": ["Inter"],
                        "label-sm": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        body { font-family: 'Inter', sans-serif; }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #e2e8f0; border-radius: 10px; }
        .editor-container:focus-within { border-bottom-color: #000000; }
    </style>
</head>
<body class="bg-background text-on-surface min-h-screen flex flex-col">
<!-- TopAppBar Shell -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">Proposal Copilot</span>
<div class="h-6 w-[1px] bg-outline-variant mx-xs"></div>
<span class="font-label-md text-label-md text-on-surface-variant">Section Review: Technical Approach</span>
</div>
<div class="flex items-center gap-md">
<nav class="hidden md:flex gap-md items-center">
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container transition-colors px-xs py-base rounded" href="#">Dashboard</a>
<a class="text-primary dark:text-inverse-primary font-bold border-b-2 border-primary font-label-md text-label-md px-xs py-base" href="#">Workspace</a>
<a class="text-on-surface-variant dark:text-surface-variant font-label-md text-label-md hover:bg-surface-container transition-colors px-xs py-base rounded" href="#">Archive</a>
</nav>
<button class="material-symbols-outlined text-primary dark:text-inverse-primary" data-icon="account_circle">account_circle</button>
</div>
</header>
<!-- Main Content Canvas -->
<main class="flex-grow pt-16 pb-20 px-lg max-w-container-max mx-auto w-full grid grid-cols-12 gap-gutter">
<!-- Left: Retrieved Sources -->
<aside class="col-span-12 lg:col-span-3 pt-md space-y-md border-r border-outline-variant pr-md hidden lg:block">
<div>
<h3 class="font-label-md text-label-md text-secondary uppercase tracking-wider mb-sm">Retrieved Sources</h3>
<div class="space-y-xs overflow-y-auto max-h-[calc(100vh-250px)] custom-scrollbar">
<!-- Knowledge Base -->
<div class="p-sm bg-surface-container-low border border-outline-variant rounded-lg group hover:border-primary transition-all cursor-pointer">
<div class="flex items-start gap-xs">
<span class="material-symbols-outlined text-secondary text-[20px]" data-icon="database">database</span>
<div>
<p class="font-label-md text-label-md text-on-surface">Q3 Technical Specs.pdf</p>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1">Knowledge Base • 94% Match</p>
</div>
</div>
</div>
<!-- Web Research -->
<div class="p-sm bg-surface-container-low border border-outline-variant rounded-lg group hover:border-primary transition-all cursor-pointer">
<div class="flex items-start gap-xs">
<span class="material-symbols-outlined text-secondary text-[20px]" data-icon="language">language</span>
<div>
<p class="font-label-md text-label-md text-on-surface">Industry Security Standards 2024</p>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1">Web Search • 88% Match</p>
</div>
</div>
</div>
<!-- Internal RFP -->
<div class="p-sm bg-surface-container-low border border-outline-variant rounded-lg group hover:border-primary transition-all cursor-pointer">
<div class="flex items-start gap-xs">
<span class="material-symbols-outlined text-secondary text-[20px]" data-icon="description">description</span>
<div>
<p class="font-label-md text-label-md text-on-surface">Global RFP Requirements</p>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1">RFP Repo • 91% Match</p>
</div>
</div>
</div>
</div>
</div>
<div class="pt-sm">
<button class="w-full flex items-center justify-center gap-xs py-sm border-2 border-dashed border-outline-variant text-on-surface-variant rounded-xl hover:bg-surface-container transition-all">
<span class="material-symbols-outlined" data-icon="add">add</span>
<span class="font-label-md text-label-md">Add Context Source</span>
</button>
</div>
</aside>
<!-- Center: Generated Section Content -->
<section class="col-span-12 lg:col-span-6 pt-md">
<div class="bg-surface-container-lowest border border-outline-variant rounded-lg shadow-sm flex flex-col min-h-[700px]">
<!-- Toolbar -->
<div class="px-sm py-xs border-b border-outline-variant flex items-center justify-between bg-surface-bright rounded-t-lg">
<div class="flex items-center gap-base">
<button class="p-xs hover:bg-surface-container-high rounded transition-colors material-symbols-outlined text-[20px]" data-icon="format_bold">format_bold</button>
<button class="p-xs hover:bg-surface-container-high rounded transition-colors material-symbols-outlined text-[20px]" data-icon="format_italic">format_italic</button>
<button class="p-xs hover:bg-surface-container-high rounded transition-colors material-symbols-outlined text-[20px]" data-icon="format_list_bulleted">format_list_bulleted</button>
<div class="w-[1px] h-4 bg-outline-variant mx-xs"></div>
<button class="p-xs hover:bg-surface-container-high rounded transition-colors material-symbols-outlined text-[20px]" data-icon="link">link</button>
</div>
<div class="flex items-center gap-xs text-on-surface-variant">
<span class="font-label-sm text-label-sm">Autosaved 2m ago</span>
</div>
</div>
<!-- Editor -->
<div class="flex-grow p-lg">
<div class="max-w-[100%] mx-auto">
<h1 class="font-headline-lg text-headline-lg text-on-surface mb-sm">Technical Implementation Approach</h1>
<div class="editor-container transition-all border-b-2 border-transparent">
<p class="font-body-lg text-body-lg text-on-surface leading-relaxed mb-md">
                                Our proposed solution leverages a modern, distributed microservices architecture designed for high availability and elastic scalability. By utilizing regional clusters synchronized via low-latency data planes, we ensure that the global user base experiences sub-100ms response times for all critical transaction paths.
                            </p>
<p class="font-body-lg text-body-lg text-on-surface leading-relaxed mb-md">
                                Security is embedded into the core of our deployment cycle. Following a "Security by Design" philosophy, every component undergoes automated static analysis and dynamic fuzzing prior to production release. Our SOC2 Type II compliance framework provides the necessary oversight to maintain strict data residency requirements for international expansion.
                            </p>
<div class="p-md bg-surface-container rounded-lg border-l-4 border-primary my-md">
<p class="font-label-md text-label-md text-primary mb-1">AI INSIGHT</p>
<p class="font-body-md text-body-md text-on-surface-variant">
                                    I've included the specific latency metrics from the Q3 Technical Specs to strengthen the groundedness of this section.
                                </p>
</div>
<p class="font-body-lg text-body-lg text-on-surface leading-relaxed">
                                Furthermore, the integration with existing legacy systems is handled via a robust abstraction layer, mitigating risks associated with vendor lock-in and allowing for a phased migration strategy that minimizes downtime.
                            </p>
</div>
</div>
</div>
</div>
</section>
<!-- Right: Groundedness Validation Panel -->
<aside class="col-span-12 lg:col-span-3 pt-md space-y-md">
<!-- Score Card -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md shadow-sm">
<h3 class="font-label-md text-label-md text-secondary uppercase tracking-wider mb-md">Groundedness Validation</h3>
<div class="space-y-sm">
<!-- Groundedness -->
<div>
<div class="flex justify-between items-center mb-1">
<span class="font-label-md text-label-md text-on-surface">Groundedness</span>
<span class="font-label-md text-label-md text-emerald-600">98%</span>
</div>
<div class="h-1.5 w-full bg-surface-container rounded-full overflow-hidden">
<div class="h-full bg-emerald-500 rounded-full" style="width: 98%"></div>
</div>
</div>
<!-- Coverage -->
<div>
<div class="flex justify-between items-center mb-1">
<span class="font-label-md text-label-md text-on-surface">Coverage</span>
<span class="font-label-md text-label-md text-emerald-600">92%</span>
</div>
<div class="h-1.5 w-full bg-surface-container rounded-full overflow-hidden">
<div class="h-full bg-emerald-500 rounded-full" style="width: 92%"></div>
</div>
</div>
<!-- Knowledge Alignment -->
<div>
<div class="flex justify-between items-center mb-1">
<span class="font-label-md text-label-md text-on-surface">Knowledge Alignment</span>
<span class="font-label-md text-label-md text-emerald-600">95%</span>
</div>
<div class="h-1.5 w-full bg-surface-container rounded-full overflow-hidden">
<div class="h-full bg-emerald-500 rounded-full" style="width: 95%"></div>
</div>
</div>
</div>
<!-- Alert -->
<div class="mt-lg p-sm bg-emerald-50 border border-emerald-100 rounded-lg flex items-center gap-xs">
<span class="material-symbols-outlined text-emerald-600" data-icon="check_circle">check_circle</span>
<div>
<p class="font-label-md text-label-md text-emerald-800">Hallucination Risk: Low</p>
<p class="font-body-sm text-body-sm text-emerald-700">Content aligns with provided sources.</p>
</div>
</div>
</div>
<!-- Context Visual Placeholder -->
<div class="relative h-48 rounded-xl overflow-hidden border border-outline-variant bg-surface-container flex items-center justify-center">

<div class="relative z-10 text-center px-md">
<span class="material-symbols-outlined text-secondary-container mb-xs" data-icon="auto_awesome">auto_awesome</span>
<p class="font-label-sm text-label-sm text-on-surface-variant">Real-time analysis active. Validating claims against 12 knowledge nodes.</p>
</div>
</div>
</aside>
</main>
<!-- BottomNavBar Shell (Actions) -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<div class="flex items-center gap-md">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all rounded-lg group">
<span class="material-symbols-outlined mr-xs group-active:scale-95 duration-150" data-icon="arrow_back">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all rounded-lg group">
<span class="material-symbols-outlined mr-xs group-active:scale-95 duration-150" data-icon="close">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
</div>
<div class="flex items-center gap-sm">
<button class="flex items-center justify-center px-md py-sm border border-outline text-on-surface hover:bg-surface-container-high rounded-xl transition-all font-label-md text-label-md active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs" data-icon="edit">edit</span>
                Edit
            </button>
<button class="flex items-center justify-center px-md py-sm border border-outline text-on-surface hover:bg-surface-container-high rounded-xl transition-all font-label-md text-label-md active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs" data-icon="refresh">refresh</span>
                Regenerate
            </button>
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-lg py-sm font-label-md text-label-md hover:opacity-90 active:scale-95 duration-150 shadow-sm">
<span class="material-symbols-outlined mr-xs" data-icon="verified">verified</span>
                Approve Section
            </button>
</div>
</footer>
<!-- Interactive script for demo -->
<script>
        document.querySelectorAll('[contenteditable="true"]').forEach(el => {
            el.addEventListener('focus', function() {
                this.closest('.editor-container')?.classList.add('border-primary');
            });
            el.addEventListener('blur', function() {
                this.closest('.editor-container')?.classList.remove('border-primary');
            });
        });
    </script>
</body></html>



<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Proposal Assembly Review - Proposal Copilot</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          "colors": {
            "primary-fixed-dim": "#bec6e0",
            "inverse-surface": "#2d3133",
            "surface-container-lowest": "#ffffff",
            "on-tertiary-fixed-variant": "#574425",
            "on-secondary-fixed-variant": "#38485d",
            "surface-bright": "#f7f9fb",
            "surface-container": "#eceef0",
            "on-primary-fixed-variant": "#3f465c",
            "on-secondary-container": "#54647a",
            "on-tertiary-fixed": "#271901",
            "tertiary-fixed-dim": "#dec29a",
            "secondary-fixed": "#d3e4fe",
            "tertiary": "#000000",
            "primary-container": "#131b2e",
            "surface-container-high": "#e6e8ea",
            "on-secondary": "#ffffff",
            "inverse-primary": "#bec6e0",
            "on-error": "#ffffff",
            "on-tertiary": "#ffffff",
            "surface": "#f7f9fb",
            "on-error-container": "#93000a",
            "primary-fixed": "#dae2fd",
            "tertiary-fixed": "#fcdeb5",
            "secondary-container": "#d0e1fb",
            "surface-dim": "#d8dadc",
            "on-tertiary-container": "#98805d",
            "secondary-fixed-dim": "#b7c8e1",
            "surface-tint": "#565e74",
            "outline-variant": "#c6c6cd",
            "tertiary-container": "#271901",
            "outline": "#76777d",
            "on-primary-fixed": "#131b2e",
            "on-secondary-fixed": "#0b1c30",
            "error": "#ba1a1a",
            "inverse-on-surface": "#eff1f3",
            "on-primary-container": "#7c839b",
            "on-primary": "#ffffff",
            "primary": "#000000",
            "on-surface": "#191c1e",
            "secondary": "#505f76",
            "surface-container-highest": "#e0e3e5",
            "on-background": "#191c1e",
            "on-surface-variant": "#45464d",
            "error-container": "#ffdad6",
            "surface-container-low": "#f2f4f6",
            "background": "#f7f9fb",
            "surface-variant": "#e0e3e5"
          },
          "borderRadius": {
            "DEFAULT": "0.125rem",
            "lg": "0.25rem",
            "xl": "0.5rem",
            "full": "0.75rem"
          },
          "spacing": {
            "gutter": "24px",
            "md": "24px",
            "xs": "8px",
            "base": "4px",
            "sm": "16px",
            "xl": "80px",
            "container-max": "1280px",
            "lg": "48px"
          },
          "fontFamily": {
            "headline-lg": ["Inter"],
            "headline-md": ["Inter"],
            "label-md": ["Inter"],
            "label-sm": ["Inter"],
            "body-md": ["Inter"],
            "body-lg": ["Inter"],
            "display-lg": ["Inter"],
            "body-sm": ["Inter"]
          },
          "fontSize": {
            "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
            "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
            "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
            "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
            "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
            "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
            "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
            "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
          }
        },
      },
    }
  </script>
<style>
    body { font-family: 'Inter', sans-serif; background-color: #f7f9fb; }
    .material-symbols-outlined {
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      vertical-align: middle;
    }
    .scrollbar-hide::-webkit-scrollbar { display: none; }
    .scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }
    .page-preview {
      box-shadow: 0px 4px 20px rgba(15, 23, 42, 0.05);
    }
  </style>
</head>
<body class="bg-background text-on-surface">
<!-- TopAppBar (From JSON Authority) -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">Proposal Copilot</span>
</div>
<div class="flex items-center gap-md">
<nav class="hidden md:flex items-center gap-sm h-full">
<a class="font-label-md text-label-md transition-colors hover:bg-surface-container dark:hover:bg-surface-container-highest px-sm h-16 flex items-center text-primary dark:text-inverse-primary font-bold border-b-2 border-primary" href="#">Review</a>
<a class="font-label-md text-label-md transition-colors hover:bg-surface-container dark:hover:bg-surface-container-highest px-sm h-16 flex items-center text-on-surface-variant dark:text-surface-variant" href="#">Dashboard</a>
<a class="font-label-md text-label-md transition-colors hover:bg-surface-container dark:hover:bg-surface-container-highest px-sm h-16 flex items-center text-on-surface-variant dark:text-surface-variant" href="#">Templates</a>
</nav>
<button class="material-symbols-outlined text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high rounded-full p-xs">account_circle</button>
</div>
</header>
<main class="pt-16 min-h-screen flex flex-col md:flex-row">
<!-- Left Sidebar: Proposal Sections -->
<aside class="w-full md:w-64 bg-surface border-r border-outline-variant p-sm flex-shrink-0 sticky top-16 h-[calc(100vh-64px)] overflow-y-auto">
<div class="mb-md">
<h3 class="font-label-md text-label-md text-secondary uppercase tracking-wider mb-sm px-xs">Proposal Sections</h3>
<nav class="space-y-base">
<a class="flex items-center gap-xs px-xs py-sm rounded-lg bg-secondary-container text-on-secondary-container font-medium" href="#exec-summary">
<span class="material-symbols-outlined text-[20px]">description</span>
<span class="font-body-sm text-body-sm">Executive Summary</span>
</a>
<a class="flex items-center gap-xs px-xs py-sm rounded-lg hover:bg-surface-container-low text-on-surface-variant transition-all" href="#context">
<span class="material-symbols-outlined text-[20px]">business_center</span>
<span class="font-body-sm text-body-sm">Business Context</span>
</a>
<a class="flex items-center gap-xs px-xs py-sm rounded-lg hover:bg-surface-container-low text-on-surface-variant transition-all" href="#solution">
<span class="material-symbols-outlined text-[20px]">lightbulb</span>
<span class="font-body-sm text-body-sm">Solution Strategy</span>
</a>
<a class="flex items-center gap-xs px-xs py-sm rounded-lg hover:bg-surface-container-low text-on-surface-variant transition-all" href="#architecture">
<span class="material-symbols-outlined text-[20px]">account_tree</span>
<span class="font-body-sm text-body-sm">Technical Architecture</span>
</a>
<a class="flex items-center gap-xs px-xs py-sm rounded-lg hover:bg-surface-container-low text-on-surface-variant transition-all" href="#pricing">
<span class="material-symbols-outlined text-[20px]">payments</span>
<span class="font-body-sm text-body-sm">Commercial Proposal</span>
</a>
<a class="flex items-center gap-xs px-xs py-sm rounded-lg hover:bg-surface-container-low text-on-surface-variant transition-all" href="#timeline">
<span class="material-symbols-outlined text-[20px]">calendar_month</span>
<span class="font-body-sm text-body-sm">Project Timeline</span>
</a>
</nav>
</div>
<div class="mt-xl pt-md border-t border-outline-variant">
<button class="w-full flex items-center justify-center gap-xs py-sm bg-primary text-on-primary rounded-xl font-label-md text-label-md hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined">check_circle</span>
          Approve Proposal
        </button>
</div>
</aside>
<!-- Center: Full Proposal Preview -->
<section class="flex-1 bg-surface-container-low p-sm md:p-lg overflow-y-auto scrollbar-hide">
<div class="max-w-3xl mx-auto space-y-md">
<!-- Document Page 1 -->
<div class="bg-white p-xl rounded-lg border border-outline-variant page-preview relative group min-h-[1056px]">
<!-- Action Overlays -->
<div class="absolute top-4 right-4 flex gap-xs opacity-0 group-hover:opacity-100 transition-opacity">
<button class="bg-surface p-xs rounded shadow-sm border border-outline-variant hover:bg-surface-container text-on-surface-variant flex items-center gap-1 font-label-sm text-label-sm">
<span class="material-symbols-outlined text-sm">edit</span> Edit
            </button>
<button class="bg-surface p-xs rounded shadow-sm border border-outline-variant hover:bg-surface-container text-on-surface-variant flex items-center gap-1 font-label-sm text-label-sm">
<span class="material-symbols-outlined text-sm">refresh</span> Regenerate
            </button>
</div>
<header class="mb-lg border-b-2 border-primary pb-sm">
<p class="font-label-md text-label-md text-primary mb-base">STRICTLY CONFIDENTIAL</p>
<h1 class="font-headline-lg text-headline-lg text-on-surface mb-xs">Enterprise Cloud Transformation Proposal</h1>
<p class="font-body-md text-body-md text-secondary">Prepared for: Global Logistics Solutions Inc.</p>
</header>
<section class="space-y-sm" id="exec-summary">
<h2 class="font-headline-md text-headline-md text-on-surface border-b border-outline-variant pb-base">1. Executive Summary</h2>
<p class="font-body-md text-body-md leading-relaxed text-on-surface-variant">
              This proposal outlines a comprehensive strategy to modernize Global Logistics Solutions' legacy infrastructure. Our approach focuses on high-availability cloud migration, automated CI/CD pipelines, and a robust security posture designed to scale with your international expansion goals.
            </p>
<p class="font-body-md text-body-md leading-relaxed text-on-surface-variant">
              By leveraging AI-driven analytics and serverless architectures, we anticipate a 40% reduction in operational overhead and a 25% improvement in deployment velocity within the first 12 months.
            </p>
<div class="my-md">
<img class="w-full h-48 object-cover rounded-lg" data-alt="A clean, professional data visualization dashboard displayed on a high-resolution screen in a bright, modern corporate office. The visualization shows upward trending line graphs in deep navy and emerald green, representing growth and efficiency. The lighting is soft and natural, emphasizing a mood of corporate success and technological clarity. The overall aesthetic is minimalist with ample white space." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAg-UCamoRJTfU0n2DwPSM1Y8HGDxqyEbAif3DtoC7jhRHV6nZcZyASVtOvya-FbFVLniyLB6k_rYJHVSMlvrQ_YGWfgSbhNNoZrf7GXWQuS6KzCiaGMl7GJ5Nlgw9baRBjA15yxDdY3GkMYkunLKyb_y38oeCYr5PhDZZOTBAFYZTX34btAfy-B5XYK6SwIAV13IubIFYG9wVaSU99MXwRMz4CuH3gUvFko6TVJIo8iyYTTuowaW1d">
</div>
</section>
<section class="space-y-sm mt-md" id="context">
<h2 class="font-headline-md text-headline-md text-on-surface border-b border-outline-variant pb-base">2. Business Context</h2>
<p class="font-body-md text-body-md leading-relaxed text-on-surface-variant">
              In the current landscape of global supply chain management, latency is the primary barrier to competitive advantage. Your existing monolithic system architecture creates significant bottlenecks during peak seasonal demand periods.
            </p>
</section>
</div>
<!-- Document Page 2 (Solution) -->
<div class="bg-white p-xl rounded-lg border border-outline-variant page-preview relative group min-h-[1056px]">
<section class="space-y-sm" id="solution">
<h2 class="font-headline-md text-headline-md text-on-surface border-b border-outline-variant pb-base">3. Solution Strategy</h2>
<div class="grid grid-cols-2 gap-md py-sm">
<div class="p-sm bg-surface-container-low rounded border border-outline-variant">
<h4 class="font-label-md text-label-md text-primary mb-base">Phase 1: Foundation</h4>
<p class="font-body-sm text-body-sm">Establishing core landing zones and identity management across all regions.</p>
</div>
<div class="p-sm bg-surface-container-low rounded border border-outline-variant">
<h4 class="font-label-md text-label-md text-primary mb-base">Phase 2: Migration</h4>
<p class="font-body-sm text-body-sm">Systematic refactoring of mission-critical databases to managed cloud instances.</p>
</div>
</div>
</section>
<section class="space-y-sm mt-md" id="architecture">
<h2 class="font-headline-md text-headline-md text-on-surface border-b border-outline-variant pb-base">4. Technical Architecture</h2>
<p class="font-body-md text-body-md leading-relaxed text-on-surface-variant">
              The proposed architecture utilizes a multi-AZ (Availability Zone) deployment strategy. Services are containerized using Docker and orchestrated via Kubernetes for maximum portability and resilience.
            </p>
<div class="bg-on-surface p-md rounded-lg my-md">
<!-- Placeholder for an architecture diagram/schematic look -->
<div class="h-64 border border-dashed border-outline-variant rounded flex items-center justify-center text-on-primary-container font-label-md italic">
                [High-Level Cloud Architecture Diagram]
              </div>
</div>
</section>
</div>
</div>
</section>
<!-- Right: Proposal Quality Summary -->
<aside class="w-full md:w-80 bg-surface border-l border-outline-variant p-sm md:p-md flex-shrink-0 sticky top-16 h-[calc(100vh-64px)] overflow-y-auto">
<div class="space-y-md">
<div>
<h3 class="font-label-md text-label-md text-on-surface-variant uppercase tracking-wider mb-sm">Quality Summary</h3>
<div class="p-sm bg-white border border-outline-variant rounded-xl space-y-sm">
<div class="space-y-base">
<div class="flex justify-between items-center">
<span class="font-label-md text-label-md text-secondary">Groundedness Score</span>
<span class="font-label-md text-label-md text-primary">98%</span>
</div>
<div class="w-full h-1.5 bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-emerald-600 transition-all duration-1000" style="width: 98%;"></div>
</div>
</div>
<div class="space-y-base">
<div class="flex justify-between items-center">
<span class="font-label-md text-label-md text-secondary">Coverage Score</span>
<span class="font-label-md text-label-md text-primary">85%</span>
</div>
<div class="w-full h-1.5 bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-emerald-600 transition-all duration-1000" style="width: 85%;"></div>
</div>
</div>
<div class="space-y-base">
<div class="flex justify-between items-center">
<span class="font-label-md text-label-md text-secondary">Knowledge Alignment</span>
<span class="font-label-md text-label-md text-primary">92%</span>
</div>
<div class="w-full h-1.5 bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-emerald-600 transition-all duration-1000" style="width: 92%;"></div>
</div>
</div>
</div>
</div>
<div>
<h3 class="font-label-md text-label-md text-on-surface-variant uppercase tracking-wider mb-sm">AI Suggestions</h3>
<div class="space-y-sm">
<div class="p-sm bg-surface-container-lowest border border-outline-variant rounded-lg group hover:border-primary transition-colors cursor-pointer">
<div class="flex items-start gap-xs mb-xs">
<span class="material-symbols-outlined text-primary text-[20px]">info</span>
<h4 class="font-label-md text-label-md text-on-surface">Enhance ROI section</h4>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">Adding a 3-year projected savings table would increase the confidence score by 12%.</p>
<button class="mt-sm font-label-sm text-label-sm text-primary underline underline-offset-4">Apply Suggestion</button>
</div>
<div class="p-sm bg-surface-container-lowest border border-outline-variant rounded-lg group hover:border-primary transition-colors cursor-pointer">
<div class="flex items-start gap-xs mb-xs">
<span class="material-symbols-outlined text-primary text-[20px]">warning</span>
<h4 class="font-label-md text-label-md text-on-surface">Missing RFP Requirement</h4>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">The 'Disaster Recovery RTO' requirement is mentioned but lacks specific metrics.</p>
<button class="mt-sm font-label-sm text-label-sm text-primary underline underline-offset-4">Fix Section</button>
</div>
</div>
</div>
<div class="pt-sm border-t border-outline-variant">
<button class="w-full flex items-center justify-center gap-xs py-sm border-2 border-primary text-primary rounded-xl font-label-md text-label-md hover:bg-surface-container transition-all">
<span class="material-symbols-outlined">download</span>
            Export as PDF
          </button>
</div>
</div>
</aside>
</main>
<!-- BottomNavBar (From JSON Authority) -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all">
<span class="material-symbols-outlined">arrow_back</span>
<span class="ml-xs font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all">
<span class="material-symbols-outlined">close</span>
<span class="ml-xs font-label-md text-label-md">Cancel</span>
</button>
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="mr-xs font-label-md text-label-md">Continue</span>
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</footer>
<script>
    // Subtle scroll synchronization highlighting for the sidebar
    document.addEventListener('DOMContentLoaded', () => {
      const sections = ['exec-summary', 'context', 'solution', 'architecture'];
      const navLinks = document.querySelectorAll('aside nav a');
      const container = document.querySelector('section.flex-1');

      container.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
          const element = document.getElementById(section);
          if (element) {
            const rect = element.getBoundingClientRect();
            if (rect.top >= 0 && rect.top <= 300) {
              current = section;
            }
          }
        });

        if (current) {
          navLinks.forEach(link => {
            link.classList.remove('bg-secondary-container', 'text-on-secondary-container');
            link.classList.add('hover:bg-surface-container-low', 'text-on-surface-variant');
            if (link.getAttribute('href').includes(current)) {
              link.classList.add('bg-secondary-container', 'text-on-secondary-container');
              link.classList.remove('hover:bg-surface-container-low', 'text-on-surface-variant');
            }
          });
        }
      });
    });
  </script>
</body></html>


<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
        }
        .bento-shimmer {
            background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.4) 50%, rgba(255,255,255,0) 100%);
            background-size: 200% 100%;
            animation: shimmer 3s infinite linear;
        }
        @keyframes shimmer {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
    </style>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-fixed-dim": "#bec6e0",
                        "inverse-surface": "#2d3133",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-fixed-variant": "#574425",
                        "on-secondary-fixed-variant": "#38485d",
                        "surface-bright": "#f7f9fb",
                        "surface-container": "#eceef0",
                        "on-primary-fixed-variant": "#3f465c",
                        "on-secondary-container": "#54647a",
                        "on-tertiary-fixed": "#271901",
                        "tertiary-fixed-dim": "#dec29a",
                        "secondary-fixed": "#d3e4fe",
                        "tertiary": "#000000",
                        "primary-container": "#131b2e",
                        "surface-container-high": "#e6e8ea",
                        "on-secondary": "#ffffff",
                        "inverse-primary": "#bec6e0",
                        "on-error": "#ffffff",
                        "on-tertiary": "#ffffff",
                        "surface": "#f7f9fb",
                        "on-error-container": "#93000a",
                        "primary-fixed": "#dae2fd",
                        "tertiary-fixed": "#fcdeb5",
                        "secondary-container": "#d0e1fb",
                        "surface-dim": "#d8dadc",
                        "on-tertiary-container": "#98805d",
                        "secondary-fixed-dim": "#b7c8e1",
                        "surface-tint": "#565e74",
                        "outline-variant": "#c6c6cd",
                        "tertiary-container": "#271901",
                        "outline": "#76777d",
                        "on-primary-fixed": "#131b2e",
                        "on-secondary-fixed": "#0b1c30",
                        "error": "#ba1a1a",
                        "inverse-on-surface": "#eff1f3",
                        "on-primary-container": "#7c839b",
                        "on-primary": "#ffffff",
                        "primary": "#000000",
                        "on-surface": "#191c1e",
                        "secondary": "#505f76",
                        "surface-container-highest": "#e0e3e5",
                        "on-background": "#191c1e",
                        "on-surface-variant": "#45464d",
                        "error-container": "#ffdad6",
                        "surface-container-low": "#f2f4f6",
                        "background": "#f7f9fb",
                        "surface-variant": "#e0e3e5"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "md": "24px",
                        "xs": "8px",
                        "base": "4px",
                        "sm": "16px",
                        "xl": "80px",
                        "container-max": "1280px",
                        "lg": "48px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "label-md": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"]
                    },
                    "fontSize": {
                        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}]
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-background text-on-surface min-h-screen flex flex-col items-center justify-center relative overflow-hidden">
<!-- Top Navigation Anchor -->
<nav class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface border-b border-outline-variant">
<div class="font-headline-md text-headline-md font-bold text-on-surface">Proposal Copilot</div>
<div class="flex items-center gap-md">
<div class="material-symbols-outlined text-primary" data-icon="account_circle">account_circle</div>
</div>
</nav>
<!-- Background Decorative Element -->
<div class="absolute inset-0 z-0 opacity-30 pointer-events-none">
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-gradient-to-br from-secondary-container to-transparent rounded-full blur-[120px]"></div>
</div>
<!-- Main Content Canvas -->
<main class="relative z-10 w-full max-w-[720px] px-md py-xl text-center">
<!-- Success Icon Section -->
<div class="mb-lg inline-flex items-center justify-center w-20 h-20 bg-primary text-on-primary rounded-full shadow-lg">
<span class="material-symbols-outlined text-[40px]" data-icon="check_circle">check_circle</span>
</div>
<div class="mb-sm">
<h1 class="font-headline-lg text-headline-lg text-on-surface mb-xs">Proposal Successfully Generated</h1>
<div class="h-1 w-24 bg-primary mx-auto rounded-full"></div>
</div>
<p class="font-body-lg text-body-lg text-secondary mb-xl max-w-[540px] mx-auto">
            Would you like to generate an Executive Summary for this proposal?
        </p>
<!-- Asymmetric Bento-style Interaction Grid -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-md mb-xl">
<!-- Main Action Card -->
<div class="md:col-span-2 group bg-surface-container-lowest border border-outline-variant p-lg rounded-xl flex flex-col items-start text-left transition-all hover:shadow-xl hover:-translate-y-1 cursor-pointer">
<div class="w-12 h-12 bg-primary-container rounded-lg flex items-center justify-center mb-md">
<span class="material-symbols-outlined text-on-primary-fixed-variant" data-icon="auto_awesome">auto_awesome</span>
</div>
<h3 class="font-headline-md text-headline-md mb-xs">Generate Executive Summary</h3>
<p class="font-body-md text-body-md text-secondary mb-lg">AI will synthesize your entire 40-page document into a high-impact, one-page summary for decision-makers.</p>
<button class="mt-auto w-full py-md bg-primary text-on-primary font-label-md text-label-md rounded-lg flex items-center justify-center gap-xs transition-colors hover:bg-opacity-90 active:scale-95">
                    Start AI Synthesis
                    <span class="material-symbols-outlined text-md" data-icon="arrow_forward">arrow_forward</span>
</button>
</div>
<!-- Context Card -->
<div class="md:col-span-1 bg-surface-container p-md rounded-xl border border-outline-variant flex flex-col items-center justify-center text-center">
<div class="w-full aspect-square relative overflow-hidden rounded-lg mb-md bg-white border border-outline-variant">
<img class="absolute inset-0 w-full h-full object-cover" data-alt="A professional overhead shot of a clean white office desk featuring a minimalist tablet displaying a complex data dashboard with elegant green progress bars and dark navy accents. The lighting is bright and airy, conveying a sense of corporate clarity and modern enterprise efficiency." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBsoxI-nPiGk24jXUw28FpUdv_y1t32tijrDYGHp5HDNaXTkWj1PMw4eRxSdV7aJpun1gwRxsxZjV8UeZesq_3sMvbLBwKlesMuim5omZ5KS3n_yv7yfSLCF1rIIc-DYXrShor5sb9A727kpRRDBuO85ol-4tWYImNAoav8d0kKS94_Xv9Yo7jxGZUIWmuQL1hhglCYX8MChrgcnMLImiFvDv8x8zxVn8nFUh0yfy3ojTyBGcs5l29C">
<div class="absolute inset-0 bg-primary/5"></div>
</div>
<span class="font-label-md text-label-md text-secondary uppercase tracking-widest mb-base">Proposal Status</span>
<span class="font-headline-md text-headline-md text-on-surface">Ready to Ship</span>
</div>
</div>
<!-- Secondary Actions -->
<div class="flex flex-col md:flex-row items-center justify-center gap-md">
<button class="flex items-center gap-xs px-lg py-sm text-secondary font-label-md text-label-md hover:text-primary transition-colors hover:bg-surface-container rounded-lg">
<span class="material-symbols-outlined" data-icon="close">close</span>
                Skip for Now
            </button>
<button class="flex items-center gap-xs px-lg py-sm text-secondary font-label-md text-label-md hover:text-primary transition-colors hover:bg-surface-container rounded-lg">
<span class="material-symbols-outlined" data-icon="visibility">visibility</span>
                Review Proposal
            </button>
</div>
</main>
<!-- Bottom Action Shell (Filtered for Transactional Focus) -->
<footer class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest border-t border-outline-variant shadow-md">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs" data-icon="arrow_back">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<div class="flex gap-md">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined mr-xs" data-icon="close">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
<button class="flex items-center justify-center bg-primary text-on-primary rounded-xl px-sm py-xs hover:bg-opacity-90 active:scale-95 duration-150">
<span class="font-label-md text-label-md">Continue</span>
<span class="material-symbols-outlined ml-xs" data-icon="arrow_forward">arrow_forward</span>
</button>
</div>
</footer>
<!-- Micro-interaction Scripts -->
<script>
        document.addEventListener('DOMContentLoaded', () => {
            const primaryCard = document.querySelector('.group');
            if (primaryCard) {
                primaryCard.addEventListener('click', () => {
                    primaryCard.classList.add('scale-95');
                    setTimeout(() => primaryCard.classList.remove('scale-95'), 150);
                });
            }
        });
    </script>
</body></html>

<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Executive Summary Review | Proposal Copilot</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-fixed-dim": "#bec6e0",
                        "inverse-surface": "#2d3133",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-fixed-variant": "#574425",
                        "on-secondary-fixed-variant": "#38485d",
                        "surface-bright": "#f7f9fb",
                        "surface-container": "#eceef0",
                        "on-primary-fixed-variant": "#3f465c",
                        "on-secondary-container": "#54647a",
                        "on-tertiary-fixed": "#271901",
                        "tertiary-fixed-dim": "#dec29a",
                        "secondary-fixed": "#d3e4fe",
                        "tertiary": "#000000",
                        "primary-container": "#131b2e",
                        "surface-container-high": "#e6e8ea",
                        "on-secondary": "#ffffff",
                        "inverse-primary": "#bec6e0",
                        "on-error": "#ffffff",
                        "on-tertiary": "#ffffff",
                        "surface": "#f7f9fb",
                        "on-error-container": "#93000a",
                        "primary-fixed": "#dae2fd",
                        "tertiary-fixed": "#fcdeb5",
                        "secondary-container": "#d0e1fb",
                        "surface-dim": "#d8dadc",
                        "on-tertiary-container": "#98805d",
                        "secondary-fixed-dim": "#b7c8e1",
                        "surface-tint": "#565e74",
                        "outline-variant": "#c6c6cd",
                        "tertiary-container": "#271901",
                        "outline": "#76777d",
                        "on-primary-fixed": "#131b2e",
                        "on-secondary-fixed": "#0b1c30",
                        "error": "#ba1a1a",
                        "inverse-on-surface": "#eff1f3",
                        "on-primary-container": "#7c839b",
                        "on-primary": "#ffffff",
                        "primary": "#000000",
                        "on-surface": "#191c1e",
                        "secondary": "#505f76",
                        "surface-container-highest": "#e0e3e5",
                        "on-background": "#191c1e",
                        "on-surface-variant": "#45464d",
                        "error-container": "#ffdad6",
                        "surface-container-low": "#f2f4f6",
                        "background": "#f7f9fb",
                        "surface-variant": "#e0e3e5"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "md": "24px",
                        "xs": "8px",
                        "base": "4px",
                        "sm": "16px",
                        "xl": "80px",
                        "container-max": "1280px",
                        "lg": "48px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "label-md": ["Inter"],
                        "label-sm": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "label-sm": ["12px", {"lineHeight": "16px", "fontWeight": "500"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
                    }
                }
            }
        }
    </script>
<style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f7f9fb;
            color: #191c1e;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .editor-paper {
            box-shadow: 0px 4px 20px rgba(15, 23, 42, 0.05);
        }
        .quality-indicator-bar {
            height: 4px;
            border-radius: 2px;
            background-color: #e2e8f0;
            overflow: hidden;
        }
        .quality-indicator-fill {
            height: 100%;
            background-color: #10b981;
            transition: width 1s ease-out;
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
    </style>
</head>
<body class="bg-background min-h-screen flex flex-col">
<!-- Top Navigation Bar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface border-b border-outline-variant">
<div class="flex items-center gap-sm">
<span class="font-headline-md text-headline-md font-bold text-on-surface">Proposal Copilot</span>
<div class="h-6 w-[1px] bg-outline-variant mx-xs"></div>
<span class="font-label-md text-label-md text-on-surface-variant">Review Mode</span>
</div>
<div class="flex items-center gap-md">
<button class="material-symbols-outlined text-on-surface-variant hover:bg-surface-container transition-colors p-xs rounded-full">search</button>
<button class="material-symbols-outlined text-on-surface-variant hover:bg-surface-container transition-colors p-xs rounded-full">account_circle</button>
</div>
</header>
<!-- Main Content Area -->
<main class="flex-grow pt-16 pb-24 max-w-container-max mx-auto w-full px-lg">
<div class="grid grid-cols-1 lg:grid-cols-3 gap-lg mt-lg">
<!-- Left Column: Executive Summary Content (2/3) -->
<div class="lg:col-span-2 flex flex-col gap-sm">
<div class="bg-surface-container-lowest p-xl rounded-lg border border-outline-variant editor-paper min-h-[800px]">
<div class="max-w-3xl mx-auto">
<header class="mb-lg border-b border-outline-variant pb-md">
<h1 class="font-headline-lg text-headline-lg text-primary mb-xs">Executive Summary</h1>
<p class="font-body-sm text-body-sm text-secondary">Strategic Expansion Proposal: Q4 Enterprise Initiative</p>
</header>
<!-- Content Sections -->
<div class="space-y-lg">
<section>
<h2 class="font-label-md text-label-md uppercase tracking-wider text-secondary mb-sm">Business Challenge</h2>
<p class="font-body-lg text-body-lg text-on-surface leading-relaxed">
                                    Current market volatility necessitates a robust digital transformation strategy to maintain competitive advantage. The organization faces fragmented data silos and inefficient procurement workflows that result in a 15% increase in operational overhead annually.
                                </p>
</section>
<section>
<h2 class="font-label-md text-label-md uppercase tracking-wider text-secondary mb-sm">Proposed Solution</h2>
<p class="font-body-lg text-body-lg text-on-surface leading-relaxed">
                                    Implementation of an AI-driven Proposal Copilot designed to unify document generation and procurement analytics. This solution leverages machine learning to automate RFP responses and provide real-time strategic context to the sales and operations teams.
                                </p>
</section>
<section>
<h2 class="font-label-md text-label-md uppercase tracking-wider text-secondary mb-sm">Expected Benefits</h2>
<ul class="list-disc pl-md font-body-lg text-body-lg text-on-surface space-y-xs">
<li>Reduces proposal turnaround time by 40% through automated drafting.</li>
<li>Increases win rates by 12% via enhanced competitive intelligence.</li>
<li>Projected annual savings of $1.2M in operational labor costs.</li>
</ul>
</section>
<section>
<h2 class="font-label-md text-label-md uppercase tracking-wider text-secondary mb-sm">Timeline</h2>
<div class="flex items-center gap-md py-sm">
<div class="flex flex-col border-l-4 border-primary pl-md">
<span class="font-label-sm text-label-sm text-secondary">Phase 1: Integration</span>
<span class="font-body-md text-body-md font-semibold">Weeks 1-4</span>
</div>
<div class="flex flex-col border-l-4 border-outline-variant pl-md">
<span class="font-label-sm text-label-sm text-secondary">Phase 2: Training</span>
<span class="font-body-md text-body-md font-semibold">Weeks 5-8</span>
</div>
<div class="flex flex-col border-l-4 border-outline-variant pl-md">
<span class="font-label-sm text-label-sm text-secondary">Phase 3: Launch</span>
<span class="font-body-md text-body-md font-semibold">Week 9</span>
</div>
</div>
</section>
<section class="bg-surface-container-low p-md rounded-xl">
<h2 class="font-label-md text-label-md uppercase tracking-wider text-secondary mb-sm">Investment Summary</h2>
<div class="flex justify-between items-end">
<div>
<span class="font-display-lg text-display-lg text-primary">$185,000</span>
<span class="font-body-md text-body-md text-secondary ml-xs">Total Enterprise Investment</span>
</div>
<div class="text-right">
<span class="font-label-sm text-label-sm text-secondary block">ROI Projection</span>
<span class="font-headline-md text-headline-md text-on-primary-container">310%</span>
</div>
</div>
</section>
</div>
</div>
</div>
</div>
<!-- Right Column: Summary Quality Indicators (1/3) -->
<div class="lg:col-span-1 space-y-md">
<div class="bg-white border border-outline-variant rounded-lg p-md sticky top-[88px]">
<div class="flex items-center justify-between mb-md">
<h3 class="font-headline-md text-headline-md text-primary">Summary Quality</h3>
<span class="material-symbols-outlined text-secondary">analytics</span>
</div>
<div class="space-y-sm">
<!-- Indicator: Coverage -->
<div class="space-y-xs">
<div class="flex justify-between items-center">
<span class="font-label-md text-label-md text-on-surface">Coverage</span>
<span class="font-label-md text-label-md text-primary">94%</span>
</div>
<div class="quality-indicator-bar">
<div class="quality-indicator-fill" style="width: 94%"></div>
</div>
<p class="font-label-sm text-label-sm text-secondary">All key requirements from RFP have been addressed.</p>
</div>
<!-- Indicator: Business Alignment -->
<div class="space-y-xs">
<div class="flex justify-between items-center">
<span class="font-label-md text-label-md text-on-surface">Business Alignment</span>
<span class="font-label-md text-label-md text-primary">88%</span>
</div>
<div class="quality-indicator-bar">
<div class="quality-indicator-fill" style="width: 88%"></div>
</div>
<p class="font-label-sm text-label-sm text-secondary">Messaging matches the client's strategic goals.</p>
</div>
<!-- Indicator: Readability -->
<div class="space-y-xs">
<div class="flex justify-between items-center">
<span class="font-label-md text-label-md text-on-surface">Readability</span>
<span class="font-label-md text-label-md text-primary">91%</span>
</div>
<div class="quality-indicator-bar">
<div class="quality-indicator-fill" style="width: 91%"></div>
</div>
<p class="font-label-sm text-label-sm text-secondary">Content is concise and avoids excessive jargon.</p>
</div>
</div>
<div class="mt-lg pt-lg border-t border-outline-variant">
<h4 class="font-label-md text-label-md text-on-surface mb-sm">AI Copilot Insights</h4>
<div class="bg-surface-container-low p-sm rounded-lg flex gap-sm border border-outline-variant">
<span class="material-symbols-outlined text-primary-container">info</span>
<p class="font-body-sm text-body-sm text-on-surface-variant">The "Investment Summary" section is particularly strong, using concrete ROI data which usually increases approval speed by 20%.</p>
</div>
</div>
</div>
<!-- Secondary Contextual Card -->
<div class="bg-white border border-outline-variant rounded-lg overflow-hidden">
<div class="relative h-40">
<img class="w-full h-full object-cover" data-alt="A clean, professional boardroom setting with high-end glass walls and a large oak table. The lighting is bright and natural, coming from large floor-to-ceiling windows. The aesthetic is modern corporate, focusing on trust and clarity. Soft shadows play across the minimalist decor, reinforcing the efficient chief of staff design theme with a palette of deep navy and slate grays." src="https://lh3.googleusercontent.com/aida-public/AB6AXuC8mjhoj0WGMDaf8NHYjnG0loWhda7ijQgNF2BttmGPfVGfLuHGUMIIBM2YXsnblQCd6OcpmbyxwnkrYJ7756Q9-0MIxjhqMupWQnrXmz5bbnoR7twmZ7DOX4KtGlQQxXiH93qI1hlzsmRz0PT9oXtoKQlyVlPBmgu3uGH7qhLOElYIHiwd55gJkwSZKPYmUs6VhyYznlaNhGQCjpkMmQVR6mQU3Qq5TWxDdtegFgtyruxjHtQLk5Y-">
<div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-md">
<span class="font-label-md text-label-md text-white">Client Context: Global Logistics Corp</span>
</div>
</div>
</div>
</div>
</div>
</main>
<!-- Bottom Navigation Bar (Actions) -->
<nav class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest border-t border-outline-variant shadow-md">
<div class="flex gap-md">
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all rounded-xl gap-xs">
<span class="material-symbols-outlined">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary px-sm py-xs hover:bg-surface-container-high transition-all rounded-xl gap-xs">
<span class="material-symbols-outlined">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
</div>
<div class="flex gap-md">
<button class="flex items-center justify-center text-primary px-md py-xs border border-outline hover:bg-surface-container-high transition-all rounded-xl gap-xs">
<span class="material-symbols-outlined">edit</span>
<span class="font-label-md text-label-md">Edit</span>
</button>
<button class="flex items-center justify-center text-primary px-md py-xs border border-outline hover:bg-surface-container-high transition-all rounded-xl gap-xs">
<span class="material-symbols-outlined">refresh</span>
<span class="font-label-md text-label-md">Regenerate</span>
</button>
<button class="flex items-center justify-center bg-primary text-on-primary rounded-xl px-lg py-xs hover:opacity-80 transition-all scale-105 active:scale-95 gap-xs">
<span class="font-label-md text-label-md">Approve</span>
<span class="material-symbols-outlined">arrow_forward</span>
</button>
</div>
</nav>
<script>
        // Simple interactive feedback for quality bars
        document.addEventListener('DOMContentLoaded', () => {
            const bars = document.querySelectorAll('.quality-indicator-fill');
            bars.forEach(bar => {
                const targetWidth = bar.style.width;
                bar.style.width = '0';
                setTimeout(() => {
                    bar.style.width = targetWidth;
                }, 300);
            });
        });

        // Hover lift effect for cards
        const interactiveCards = document.querySelectorAll('.bg-white.border');
        interactiveCards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-2px)';
                card.style.boxShadow = '0px 8px 24px rgba(15, 23, 42, 0.08)';
                card.style.transition = 'all 0.3s ease';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0)';
                card.style.boxShadow = 'none';
            });
        });
    </script>
</body></html>

<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Proposal Completed Successfully - Proposal Copilot</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-fixed-dim": "#bec6e0",
                        "inverse-surface": "#2d3133",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-fixed-variant": "#574425",
                        "on-secondary-fixed-variant": "#38485d",
                        "surface-bright": "#f7f9fb",
                        "surface-container": "#eceef0",
                        "on-primary-fixed-variant": "#3f465c",
                        "on-secondary-container": "#54647a",
                        "on-tertiary-fixed": "#271901",
                        "tertiary-fixed-dim": "#dec29a",
                        "secondary-fixed": "#d3e4fe",
                        "tertiary": "#000000",
                        "primary-container": "#131b2e",
                        "surface-container-high": "#e6e8ea",
                        "on-secondary": "#ffffff",
                        "inverse-primary": "#bec6e0",
                        "on-error": "#ffffff",
                        "on-tertiary": "#ffffff",
                        "surface": "#f7f9fb",
                        "on-error-container": "#93000a",
                        "primary-fixed": "#dae2fd",
                        "tertiary-fixed": "#fcdeb5",
                        "secondary-container": "#d0e1fb",
                        "surface-dim": "#d8dadc",
                        "on-tertiary-container": "#98805d",
                        "secondary-fixed-dim": "#b7c8e1",
                        "surface-tint": "#565e74",
                        "outline-variant": "#c6c6cd",
                        "tertiary-container": "#271901",
                        "outline": "#76777d",
                        "on-primary-fixed": "#131b2e",
                        "on-secondary-fixed": "#0b1c30",
                        "error": "#ba1a1a",
                        "inverse-on-surface": "#eff1f3",
                        "on-primary-container": "#7c839b",
                        "on-primary": "#ffffff",
                        "primary": "#000000",
                        "on-surface": "#191c1e",
                        "secondary": "#505f76",
                        "surface-container-highest": "#e0e3e5",
                        "on-background": "#191c1e",
                        "on-surface-variant": "#45464d",
                        "error-container": "#ffdad6",
                        "surface-container-low": "#f2f4f6",
                        "background": "#f7f9fb",
                        "surface-variant": "#e0e3e5"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "24px",
                        "md": "24px",
                        "xs": "8px",
                        "base": "4px",
                        "sm": "16px",
                        "xl": "80px",
                        "container-max": "1280px",
                        "lg": "48px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Inter"],
                        "headline-md": ["Inter"],
                        "label-md": ["Inter"],
                        "label-sm": ["Inter"],
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "headline-lg": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
                        "headline-md": ["24px", { "lineHeight": "32px", "fontWeight": "600" }],
                        "label-md": ["14px", { "lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                        "label-sm": ["12px", { "lineHeight": "16px", "fontWeight": "500" }],
                        "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }],
                        "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
                        "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "body-sm": ["14px", { "lineHeight": "20px", "fontWeight": "400" }]
                    }
                },
            },
        }
    </script>
<style>
        body { font-family: 'Inter', sans-serif; }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .success-bg-pattern {
            background-color: #f7f9fb;
            background-image: radial-gradient(#eceef0 1px, transparent 1px);
            background-size: 32px 32px;
        }
    </style>
</head>
<body class="bg-background text-on-background min-h-screen flex flex-col success-bg-pattern">
<!-- TopAppBar -->
<header class="fixed top-0 w-full z-50 flex justify-between items-center px-lg h-16 max-w-container-max mx-auto bg-surface dark:bg-inverse-surface border-b border-outline-variant dark:border-outline">
<div class="font-headline-md text-headline-md font-bold text-on-surface dark:text-inverse-on-surface">
            Proposal Copilot
        </div>
<div class="flex items-center gap-md">
<button class="material-symbols-outlined text-primary dark:text-inverse-primary hover:bg-surface-container dark:hover:bg-surface-container-highest transition-colors p-base rounded-full" data-icon="account_circle">account_circle</button>
</div>
</header>
<!-- Main Content Canvas -->
<main class="flex-grow flex items-center justify-center pt-16 pb-24 px-md">
<div class="max-w-[800px] w-full flex flex-col items-center text-center">
<!-- Success Branding Header -->
<div class="mb-lg animate-in fade-in slide-in-from-bottom-4 duration-700">
<div class="w-24 h-24 bg-primary text-on-primary rounded-full flex items-center justify-center mx-auto mb-sm shadow-lg">
<span class="material-symbols-outlined text-[48px]" style="font-variation-settings: 'FILL' 1;">check_circle</span>
</div>
<h1 class="font-headline-lg text-headline-lg text-on-surface mb-xs">Proposal Completed Successfully</h1>
<p class="font-body-lg text-body-lg text-secondary max-w-lg mx-auto">Your proposal has been validated, formatted, and is ready for final delivery.</p>
</div>
<!-- Bento-style Deliverables Grid -->
<div class="w-full grid grid-cols-1 md:grid-cols-3 gap-sm mb-lg animate-in fade-in slide-in-from-bottom-8 duration-700 delay-150">
<!-- Deliverable Item 1 -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col items-center hover:shadow-md transition-shadow group">
<div class="p-sm bg-surface-container-low rounded-full mb-sm group-hover:bg-primary group-hover:text-on-primary transition-colors">
<span class="material-symbols-outlined text-[32px]" data-icon="description">description</span>
</div>
<span class="font-label-md text-label-md text-on-surface mb-base">Proposal Document</span>
<span class="font-body-sm text-body-sm text-secondary">Main full proposal</span>
</div>
<!-- Deliverable Item 2 -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col items-center hover:shadow-md transition-shadow group">
<div class="p-sm bg-surface-container-low rounded-full mb-sm group-hover:bg-primary group-hover:text-on-primary transition-colors">
<span class="material-symbols-outlined text-[32px]" data-icon="summarize">summarize</span>
</div>
<span class="font-label-md text-label-md text-on-surface mb-base">Executive Summary</span>
<span class="font-body-sm text-body-sm text-secondary">High-level overview</span>
</div>
<!-- Deliverable Item 3 -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-md flex flex-col items-center hover:shadow-md transition-shadow group">
<div class="p-sm bg-surface-container-low rounded-full mb-sm group-hover:bg-primary group-hover:text-on-primary transition-colors">
<span class="material-symbols-outlined text-[32px]" data-icon="verified">verified</span>
</div>
<span class="font-label-md text-label-md text-on-surface mb-base">Quality Validation Report</span>
<span class="font-body-sm text-body-sm text-secondary">AI consistency check</span>
</div>
</div>
<!-- Action Cluster -->
<div class="w-full space-y-md animate-in fade-in slide-in-from-bottom-12 duration-700 delay-300">
<div class="flex flex-col sm:flex-row gap-md justify-center">
<button class="bg-primary text-on-primary font-label-md text-label-md px-lg py-sm rounded-lg flex items-center justify-center gap-xs hover:opacity-90 active:scale-95 transition-all shadow-sm">
<span class="material-symbols-outlined" data-icon="picture_as_pdf">picture_as_pdf</span>
                        Download PDF
                    </button>
<button class="bg-surface-container-highest text-on-surface font-label-md text-label-md px-lg py-sm rounded-lg flex items-center justify-center gap-xs hover:bg-surface-dim active:scale-95 transition-all border border-outline-variant">
<span class="material-symbols-outlined" data-icon="article">article</span>
                        Download DOCX
                    </button>
</div>
<div class="flex flex-wrap gap-sm justify-center pt-md border-t border-outline-variant">
<button class="flex items-center gap-xs text-secondary hover:text-primary transition-colors px-sm py-xs">
<span class="material-symbols-outlined text-[20px]" data-icon="ios_share">ios_share</span>
<span class="font-label-md text-label-md">Export Proposal</span>
</button>
<button class="flex items-center gap-xs text-secondary hover:text-primary transition-colors px-sm py-xs">
<span class="material-symbols-outlined text-[20px]" data-icon="add_circle">add_circle</span>
<span class="font-label-md text-label-md">Create New Proposal</span>
</button>
</div>
</div>
<!-- Atmospheric Decoration -->
<div class="mt-xl opacity-20 pointer-events-none">
<div class="w-full h-px bg-gradient-to-r from-transparent via-outline to-transparent"></div>
<div class="flex justify-center gap-xl mt-md">
<span class="material-symbols-outlined text-[48px]" data-icon="auto_awesome">auto_awesome</span>
<span class="material-symbols-outlined text-[48px]" data-icon="history_edu">history_edu</span>
<span class="material-symbols-outlined text-[48px]" data-icon="architecture">architecture</span>
</div>
</div>
</div>
</main>
<!-- BottomNavBar (Suppressed due to Success Screen / Transactional focus but keeping for consistency if requested by shell rules; prompt says 'Back/Cancel/Continue' in JSON but contextually 'Create New' or 'Finish' would fit. Following JSON mapping literally as instructed) -->
<nav class="fixed bottom-0 w-full z-50 flex justify-between items-center px-lg py-md max-w-container-max mx-auto bg-surface-container-lowest dark:bg-inverse-surface border-t border-outline-variant dark:border-outline shadow-md">
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs" data-icon="arrow_back">arrow_back</span>
<span class="font-label-md text-label-md">Back</span>
</button>
<button class="flex items-center justify-center text-secondary dark:text-secondary-fixed-dim px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="material-symbols-outlined mr-xs" data-icon="close">close</span>
<span class="font-label-md text-label-md">Cancel</span>
</button>
<!-- Mapping 'Continue' to the Primary Completion action -->
<button class="flex items-center justify-center bg-primary dark:bg-primary-fixed text-on-primary dark:text-on-primary-fixed rounded-xl px-sm py-xs hover:bg-surface-container-high dark:hover:bg-surface-container transition-all active:scale-95 duration-150">
<span class="font-label-md text-label-md mr-xs">Continue</span>
<span class="material-symbols-outlined" data-icon="arrow_forward">arrow_forward</span>
</button>
</nav>
<!-- Visual Polish: Floating Animation -->
<div class="fixed inset-0 pointer-events-none overflow-hidden z-[-1] opacity-50">

</div>
<script>
        // Micro-interactions for button feedback
        document.querySelectorAll('button').forEach(button => {
            button.addEventListener('mousedown', () => {
                button.classList.add('scale-95');
            });
            button.addEventListener('mouseup', () => {
                button.classList.remove('scale-95');
            });
            button.addEventListener('mouseleave', () => {
                button.classList.remove('scale-95');
            });
        });

        // Simulating the success icon pop
        window.addEventListener('DOMContentLoaded', () => {
            const successIcon = document.querySelector('.w-24.h-24');
            successIcon.classList.add('animate-bounce');
            setTimeout(() => {
                successIcon.classList.remove('animate-bounce');
            }, 1000);
        });
    </script>
</body></html>

