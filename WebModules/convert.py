import pyraphrase

pdf_said = """be assigned. A study showed that informal mentors
typically were more helpful to a persons career than
formal mentors, and informal mentoring is also associated
with higher income. The human resource
department often coordinates a formal mentoring
program. Shadowing is a form of mentoring. Mentors
enhance the career of proteges in many ways,
such as by recommending them for promotion and
helping them establish valuable contacts. Also, the
mentor can serve as a model for effective (or ineffective)
leadership.
Feedback-intensive development programs help
leaders develop by seeing more clearly their patterns
of behavior, the reasons for such behaviors, and the
impact of these behaviors and attitudes on their
effectiveness. Skill training in leadership development
involves acquiring abilities and techniques that
can be converted into action. Such training involves
a considerable element of "how to." Five methods of
skill-based training are lecture, case study, role play,
behavior role modeling, and simulations. During
simulations, participants play the role of company
leaders and devise solutions to problems. Feedback
on performance is provided.
A standard university approach to leadership development
is to equip people with a conceptual understanding
of leadership. The concepts can be applied
to leadership situations. Personal growth experiences
for leadership development assume that leaders
are deeply in touch with their personal dreams and
talents and will act to fulfill them. Another emphasis
in these programs is learning who you need to be.
From the company standpoint, an essential type of
leadership development is becoming socialized in
the company vision and values. Action learning is a
directly practical approach to leadership development
and may be directed at areas outside the participants
expertise. Coaching and psychotherapy are two highly
personal ways of developing as a leader. Psychotherapy
is called for when the leader has emotional
problems that lower his or her effectiveness.
Leadership succession is linked to leadership
development because being groomed as a successor
is part of a leader's development. Boards of directors
use standard selection methods in choosing a CEO.
In addition, they look for both formal and informal
contact with insiders. When recruiting an outsider,
organizations often employ executive search firms.
General Electric is an example of a company that
uses rigorous succession planning. Leadership
succession is highly emotional for the leader who
is being replaced, especially when a founder sells a
business. The succession problem in a family business
often leads to conflict among family members.
Large family-run businesses are more likely to
identify leadership successors. One way to cope with
potential shortages of leaders is to identify a pool
of high-potential individuals and provide them with
developmental experiences. Recent research and
analysis suggest that promoting company insiders
with an outside perspective may be the best solution
to succession through an internal versus an external
candidate."""

converted_pdf = pdf_said.replace("\n"," ")
print(converted_pdf)
