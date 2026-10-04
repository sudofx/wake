/*
 * WAKE✳︎ plain-language help.
 * Explanations describe the visible interface without adding authority or claims.
 */
(() => {
  'use strict';

  const topics = {
    blog: ["Bob’s Blog","Selected plain-language notes about work already recorded by WAKE✳︎.","Read the post first. Follow its notebook, evidence, and history links when you want the underlying record.","Bob is a public writing voice, not a separate agent or persistent identity.","Posts summarize recorded work; they do not create research authority."],
    projects: ["Projects","Focused research questions that WAKE✳︎ is actively tracking.","Status shows where the work stands. Next step shows what the project is trying to do next.","Projects turn broad topics into inspectable work with a durable trail.","A project can change direction without erasing its earlier record."],
    journal: ["Journal","A readable timeline of accepted work across separate model invocations.","Treat each entry as a new model call continuing from the durable record left by earlier calls.","The journal shows continuity of work without requiring hidden model memory.","Accepted means the change passed governance; it does not mean every claim is true."],
    field_notes: ["Journal entry","A plain-language summary of changes accepted in one wake.","Read what changed, why it changed, and which model proposed it.","It gives the technical event history a human-readable layer.","The exact event record remains the audit source underneath."],
    continuity_question: ["Continuity","WAKE✳︎ tests whether useful work can continue when models, sessions, vendors, or people change.","Look for objectives, evidence, open commitments, decisions, and receipts carried forward through the record.","The durable record—not a model’s private memory—is what preserves continuity.","Continuity here means continuity of accountable work."],
    current_hook: ["Open commitments","Work that earlier wakes recorded as unfinished or due for review.","Use the due cycle and status to see what still needs attention.","Visible commitments make unfinished work harder to lose between model calls.","A commitment is a recorded obligation, not a promise that a model will succeed."],
    runtime_receipt: ["Context receipt","A record of what context was delivered at the model boundary.","Use it to verify what information was available to a model call.","Receipts make handoffs inspectable across providers and sessions.","Delivery does not prove understanding or correct use."],
    lab: ["Lab","The rules, tests, beliefs, commitments, and low-level records behind the public views.","Use it when you need to inspect how a result was governed or reproduced.","The Lab separates system mechanics from the friendlier reading experience.","Technical visibility supports auditability; it does not make every conclusion correct."],
    evidence: ["Evidence","Saved source material and observations used by the research workload.","Follow the source and provenance links before treating a claim as well supported.","Evidence keeps research connected to inspectable material instead of polished prose alone.","A saved source can still be incomplete, weak, outdated, or misinterpreted."],
    history: ["History","The append-only event record, including accepted, rejected, deferred, failed, and recovered work.","Read events in sequence or follow an exact wake ID.","Keeping failures and rejections makes the process auditable and correctable.","History records what happened; it is not a quality score."],
    research_pet: ["Bob","The public byline used for selected explanatory writing about WAKE✳︎ research.","Use Bob’s posts as an entry point, then follow the linked notebook and evidence trail.","A consistent public voice makes technical work easier to read.","Bob is a presentation role, not WAKE✳︎’s identity or a persistent mind."],
    visit_summary: ["Since your last visit","A browser-local summary of changes since this device last viewed the site.","Use it as a catch-up shortcut, not as part of the durable record.","It helps returning readers find recent work quickly.","This count can reset when browser storage is cleared."],
    workbench: ["Current work","Research questions with active next steps.","Open a project to see its question, current state, notebooks, and next step.","This view shows direction without hiding unfinished work.","Active does not mean close to completion."],
    latest_work: ["Latest published work","The newest notebooks that reached the publication layer.","Read findings together with limitations, evidence, and revision history.","Publication makes work readable without removing its provenance.","Published means available in the record, not proven or final."],
    specialty: ["Research distribution","A count of published notebooks by topic.","Longer bars mean more recorded output in that area.","It shows where work has accumulated over time.","More output does not mean greater expertise or truth."],
    growth: ["Recorded output","Counts of notebooks, revisions, projects, and collected sources.","Use these as activity measures only.","They show what the durable record contains and how it changes.","They do not measure intelligence, consciousness, or research quality."],
    under_hood: ["Inspect the system","Links to the rules, history, state, and operator-facing technical views.","Use these when the public summary is not enough.","The readable site and technical record are different views of the same system.","Operational state and public presentation must not be confused."],
    durable_objective: ["Durable objective","The saved objective supplied to fresh model calls.","Follow how context becomes a proposal, governance decision, transition, and receipt.","A durable objective lets different models participate in one governed process.","The objective constrains work; models cannot silently rewrite it."],
    repeatable_harness: ["Offline experiment","A deterministic test harness for continuity, governance, recovery, and replay.","Passed checks mean the software behaved as specified under the fixture experiment.","Repeatable tests help separate software guarantees from model behavior.","Fixture success does not prove live-model comprehension or research quality."],
    accepted_cycles: ["Accepted wakes","Recent model calls whose proposed changes passed governance and were recorded.","Open an exact wake to inspect context, response, decision, and receipt.","They show successful governed transitions across separate model calls.","Accepted means allowed and committed—not necessarily true."],
    beliefs: ["Working beliefs","Claims currently carried forward with confidence, evidence links, and status.","Look at supporting evidence and revision history, not only confidence.","Visible revision makes changing conclusions part of the record.","A working belief is provisional and may later be revised or retracted."],
    commitments: ["Commitments","The durable list of open and completed obligations created by earlier wakes.","Open items still require attention; resolved items retain their history.","Commitments preserve unfinished work across model boundaries.","They record accountability, not guaranteed completion."],
    notebook_shelf: ["Notebooks","Published research syntheses, including later revisions.","Read findings together with limitations, open questions, and source trails.","Notebooks are the main research output of the current reference workload.","A notebook is a governed synthesis, not settled truth."]
  };

  const layer=document.getElementById('help-layer');
  const panel=document.getElementById('help-panel');
  let returnFocus=null;
  const fields=['what','read','why','questions'];

  function button(key){
    const topic=topics[key];
    return topic ? '<button class="help-trigger" type="button" data-help="'+key+'" aria-label="Explain '+topic[0]+'" title="Plain-language explanation">?</button>' : '';
  }

  function position(trigger){
    if(!panel||!trigger)return;
    panel.style.removeProperty('--help-left');
    panel.style.removeProperty('--help-top');
    if(matchMedia('(max-width:720px)').matches)return;
    const r=trigger.getBoundingClientRect();
    const width=Math.min(420,Math.max(320,window.innerWidth*.34));
    const gap=12;
    let left=r.right+gap;
    if(left+width>window.innerWidth-18)left=Math.max(18,r.left-width-gap);
    const estimatedHeight=Math.min(470,window.innerHeight-120);
    let top=Math.max(76,Math.min(r.top-18,window.innerHeight-estimatedHeight-18));
    panel.style.setProperty('--help-left',left+'px');
    panel.style.setProperty('--help-top',top+'px');
  }

  function close(){
    layer.hidden=true;
    document.body.classList.remove('help-open');
    if(returnFocus)returnFocus.focus();
  }

  function open(key,trigger){
    const topic=topics[key];
    if(!topic)return;
    returnFocus=trigger;
    document.getElementById('help-title').textContent=topic[0];
    fields.forEach((field,index)=>document.getElementById('help-'+field).textContent=topic[index+1]);
    layer.hidden=false;
    document.body.classList.add('help-open');
    position(trigger);
    document.getElementById('help-close').focus();
  }

  document.addEventListener('click',event=>{
    const trigger=event.target.closest('[data-help]');
    if(trigger){event.preventDefault();open(trigger.dataset.help,trigger);return;}
    if(event.target===layer||event.target.closest('[data-help-close]'))close();
  });
  window.addEventListener('resize',()=>{if(!layer.hidden&&returnFocus)position(returnFocus);});
  document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!layer.hidden)close();});
  window.WakeHelp={button};
})();
