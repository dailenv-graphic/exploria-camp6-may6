#!/usr/bin/env python3
"""Generate standalone thank-you transactional emails (Orlando, Daytona, Poconos).

Icons: Material Design filled 24dp paths (same as @mui/icons-material / Google Material Icons).
Regenerate: python3 emails/build_thank_you_emails.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEGAL = (ROOT / "thank-you-legal-fragment.html").read_text(encoding="utf-8")

# Material Design Icons — filled paths (Material Icons / MUI 5.15)
MD_WARNING = (
    "M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"
)
MD_LUGGAGE = (
    "M17 6h-2V3c0-.55-.45-1-1-1h-4c-.55 0-1 .45-1 1v3H7c-1.1 0-2 .9-2 2v11c0 1.1.9 2 2 2 0 .55.45 1 1 1s1-.45 1-1h6c0 .55.45 1 1 1s1-.45 1-1c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zM9.5 18H8V9h1.5v9zm3.25 0h-1.5V9h1.5v9zm.75-12h-3V3.5h3V6zM16 18h-1.5V9H16v9z"
)
MD_ASSIGNMENT_TURNED_IN = (
    "M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm-2 14-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"
)
MD_KING_BED = (
    "M20 10V7c0-1.1-.9-2-2-2H6c-1.1 0-2 .9-2 2v3c-1.1 0-2 .9-2 2v5h1.33L4 19h1l.67-2h12.67l.66 2h1l.67-2H22v-5c0-1.1-.9-2-2-2zm-9 0H6V7h5v3zm7 0h-5V7h5v3z"
)
MD_BEDTIME = (
    "M12.34 2.02C6.59 1.82 2 6.42 2 12c0 5.52 4.48 10 10 10 3.71 0 6.93-2.02 8.66-5.02-7.51-.25-12.09-8.43-8.32-14.96z"
)
MD_GROUP = (
    "M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"
)
MD_CALENDAR_MONTH = (
    "M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2zm0 16H5V10h14v10zM9 14H7v-2h2v2zm4 0h-2v-2h2v2zm4 0h-2v-2h2v2zm-8 4H7v-2h2v2zm4 0h-2v-2h2v2zm4 0h-2v-2h2v2z"
)
MD_SAILING = (
    "M11 13.5V2L3 13.5h8zm10 0C21 6.5 14.5 1 12.5 1c0 0 1 3 1 6.5s-1 6-1 6H21zm1 1.5H2c.31 1.53 1.16 2.84 2.33 3.73.65-.27 1.22-.72 1.67-1.23.73.84 1.8 1.5 3 1.5s2.27-.66 3-1.5c.73.84 1.8 1.5 3 1.5s2.26-.66 3-1.5c.45.51 1.02.96 1.67 1.23 1.17-.89 2.02-2.2 2.33-3.73zm0 8v-2h-1c-1.04 0-2.08-.35-3-1-1.83 1.3-4.17 1.3-6 0-1.83 1.3-4.17 1.3-6 0-.91.65-1.96 1-3 1H2v2h1c1.03 0 2.05-.25 3-.75 1.89 1 4.11 1 6 0 1.89 1 4.11 1 6 0 .95.5 1.97.75 3 .75h1z"
)
MD_CREDIT_SCORE = (
    "M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h5v-2H4v-6h18V6c0-1.11-.89-2-2-2zm0 4H4V6h16v2zm-5.07 11.17-2.83-2.83-1.41 1.41L14.93 22 22 14.93l-1.41-1.41-5.66 5.65z"
)
MD_REDEEM = (
    "M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 11 8.76l1-1.36 1 1.36L15.38 12 17 10.83 14.92 8H20v6z"
)


def md_icon(path_d: str, size: int, color: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" '
        f'fill="{color}" aria-hidden="true"><path d="{path_d}"/></svg>'
    )


ICON_WARN = md_icon(MD_WARNING, 24, "#E5701C")


def icon_luggage(size: int = 24) -> str:
    return md_icon(MD_LUGGAGE, size, "#205272")


def icon_assignment_turned_in(size: int = 20) -> str:
    return md_icon(MD_ASSIGNMENT_TURNED_IN, size, "#205272")


def icon_king_bed(size: int = 20) -> str:
    return md_icon(MD_KING_BED, size, "#205272")


def icon_bedtime(size: int = 20) -> str:
    return md_icon(MD_BEDTIME, size, "#205272")


def icon_group(size: int = 20) -> str:
    return md_icon(MD_GROUP, size, "#205272")


def icon_calendar_month(size: int = 20) -> str:
    return md_icon(MD_CALENDAR_MONTH, size, "#205272")


def icon_sailing(size: int = 20) -> str:
    return md_icon(MD_SAILING, size, "#205272")


def icon_credit_score(size: int = 20) -> str:
    return md_icon(MD_CREDIT_SCORE, size, "#205272")


def icon_redeem(size: int = 20) -> str:
    return md_icon(MD_REDEEM, size, "#205272")


def summary_row(icon_html: str, label: str, value_html: str) -> str:
    return f"""
                <tr>
                  <td class="ty-summary-row" style="padding:0 0 6px;">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td class="ty-icon-cell" width="28" valign="top" style="width:28px;padding:2px 8px 0 0;line-height:0;">{icon_html}</td>
                        <td class="ty-summary-text" valign="top" style="font-family:'Inter',Arial,Helvetica,sans-serif;font-size:14px;line-height:1.5;color:#205272;word-break:break-word;">
                          <span style="font-weight:600;">{label}</span>
                          <span style="font-weight:500;">{value_html}</span>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>"""


def build_html(title: str, hero_src: str, includes_text: str, bonus_text: str) -> str:
    rows = []
    rows.append(summary_row(icon_assignment_turned_in(), "Receipt #", "&nbsp;1234567890"))
    rows.append(summary_row(icon_king_bed(), "Unit type:", "&nbsp;Standard"))
    rows.append(summary_row(icon_bedtime(), "Number of nights:", "&nbsp;3 nights"))
    rows.append(summary_row(icon_group(), "Guests:", "&nbsp;2 Adults"))
    rows.append(
        summary_row(
            icon_calendar_month(),
            "Preferred check-in:",
            '&nbsp;<a href="tel:%PHONE%" style="color:#004BFF;font-weight:700;text-decoration:underline;">Call now to book your travel dates. %PHONE%</a>',
        )
    )
    rows.append(
        summary_row(
            icon_calendar_month(),
            "Preferred check-out:",
            '&nbsp;<a href="tel:%PHONE%" style="color:#004BFF;font-weight:700;text-decoration:underline;">Call now to book your travel dates. %PHONE%</a>',
        )
    )
    rows.append(
        summary_row(
            icon_sailing(),
            "Includes:",
            f"&nbsp;{includes_text}",
        )
    )
    rows.append(
        summary_row(
            icon_credit_score(),
            "Package Price:",
            "&nbsp;$99.00&nbsp;Refundable Deposit",
        )
    )
    rows.append(
        summary_row(
            icon_redeem(),
            "Bonus Gift Details:",
            f"&nbsp;{bonus_text}",
        )
    )
    summary_inner = "\n".join(rows)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Roboto:wght@400;500&family=Montserrat:wght@400;700&display=swap" rel="stylesheet" />
  <style type="text/css">
    body {{ margin:0 !important; padding:0 !important; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; }}
    img {{ border:0; outline:none; text-decoration:none; display:block; line-height:0; }}
    table {{ border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt; }}
    .ty-action-box {{ border:0 !important; outline:none !important; }}
    /* ~390px viewports (and smaller) */
    @media only screen and (max-width: 390px) {{
      .ty-shell {{ width:100% !important; max-width:100% !important; }}
      .ty-hero-img {{ width:100% !important; max-width:100% !important; height:auto !important; }}
      .ty-paid {{ padding:14px 16px !important; }}
      .ty-paid-inner td {{ font-size:15px !important; white-space:normal !important; }}
      .ty-paid-amt {{ font-size:18px !important; }}
      .ty-pad-head {{ padding:24px 16px 0 !important; }}
      .ty-h1 {{ font-size:32px !important; letter-spacing:-0.8px !important; line-height:1.05 !important; }}
      .ty-h2 {{ font-size:18px !important; letter-spacing:0 !important; line-height:1.2 !important; }}
      .ty-intro {{ font-size:15px !important; line-height:1.45 !important; }}
      .ty-pad-action {{ padding:24px 16px 24px !important; }}
      .ty-action-inner {{ padding:18px 16px !important; outline:none !important; }}
      .ty-action-title {{ font-size:16px !important; letter-spacing:0.28px !important; }}
      .ty-action-body {{ font-size:15px !important; }}
      .ty-cta-wrap {{ width:100% !important; }}
      .ty-cta-wrap a {{ display:block !important; width:100% !important; box-sizing:border-box !important; text-align:center !important; padding:18px 16px !important; }}
      .ty-pad-summary {{ padding:24px 16px 24px !important; }}
      .ty-summary-h {{ font-size:20px !important; }}
      .ty-summary-card {{ padding:22px 16px !important; }}
      .ty-vp-title {{ font-size:16px !important; }}
      .ty-summary-text {{ font-size:13px !important; }}
      .ty-icon-cell {{ width:26px !important; max-width:26px !important; padding-right:6px !important; }}
      .ty-icon-cell svg {{ width:20px !important; height:20px !important; }}
      .ty-pad-legal {{ padding:28px 16px !important; }}
      .ty-legal-h {{ font-size:22px !important; }}
      .ty-legal-h-sm {{ font-size:17px !important; line-height:1.15 !important; }}
      .ty-legal-body {{ font-size:11px !important; line-height:1.3 !important; }}
      .ty-pad-footer {{ padding:36px 20px !important; }}
      .ty-footer-copy {{ font-size:13px !important; }}
      .ty-footer-discl {{ font-size:12px !important; }}
    }}
  </style>
</head>
<body style="margin:0;background-color:#eeeeee;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
      <td align="center" style="padding:0;">
        <table role="presentation" class="ty-shell" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background-color:#ffffff;font-family:'Inter',Arial,Helvetica,sans-serif;">

          <!-- Hero -->
          <tr>
            <td style="padding:0;line-height:0;">
              <img class="ty-hero-img" src="{hero_src}" width="600" alt="" style="width:100%;max-width:600px;height:auto;display:block;" />
            </td>
          </tr>

          <!-- Total paid bar -->
          <tr>
            <td class="ty-paid" align="center" style="padding:16px 48px;background-color:#107c8c;color:#ffffff;">
              <table role="presentation" class="ty-paid-inner" cellpadding="0" cellspacing="0" border="0" align="center">
                <tr>
                  <td style="font-family:'Inter',Arial,Helvetica,sans-serif;font-size:16px;font-weight:500;padding:0 10px 0 0;white-space:nowrap;">Total paid:</td>
                  <td class="ty-paid-amt" style="font-family:'Inter',Arial,Helvetica,sans-serif;font-size:20px;font-weight:700;white-space:nowrap;">
                    <span style="font-weight:600;">$</span> 99.00
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Headlines -->
          <tr>
            <td class="ty-pad-head" style="padding:32px 24px 0;">
              <p class="ty-h1" style="margin:0 0 24px;font-family:'Inter',Arial,Helvetica,sans-serif;font-size:48px;font-weight:800;line-height:1.04;letter-spacing:-1.5px;color:#071330;">Congrats! All set!</p>
              <p class="ty-h2" style="margin:0 0 24px;font-family:'Inter',Arial,Helvetica,sans-serif;font-size:24px;font-weight:800;line-height:1.1;letter-spacing:-0.18px;color:#071330;">Your Exploria Resorts Memories Getaway Has Been Secured!</p>
              <p class="ty-intro" style="margin:0;font-family:'Inter',Arial,Helvetica,sans-serif;font-size:16px;font-weight:500;line-height:1.5;color:#071330;">Here are your vacation package details, bonuses and the travel perks you paid for.</p>
            </td>
          </tr>

          <!-- Action required -->
          <tr>
            <td class="ty-pad-action" style="padding:32px 24px 24px;">
              <table role="presentation" class="ty-action-box" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#fffda9;border:0;border-radius:16px;outline:none;">
                <tr>
                  <td class="ty-action-inner" style="padding:24px;outline:none;border:0;">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td style="padding:0 0 24px;">
                          <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                              <td width="36" valign="middle" style="width:36px;padding:0 12px 0 0;line-height:0;">{ICON_WARN}</td>
                              <td class="ty-action-title" valign="middle" style="font-family:'Inter',Arial,Helvetica,sans-serif;font-size:18px;font-weight:700;letter-spacing:0.36px;text-transform:uppercase;color:#e5701c;">Action required</td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td class="ty-action-body" style="padding:0 0 24px;font-family:'Inter',Arial,Helvetica,sans-serif;font-size:16px;font-weight:500;line-height:1.5;color:#222222;">
                          <p style="margin:0 0 12px;">The resort requires additional details before we can confirm your travel dates.</p>
                          <p style="margin:0 0 12px;">Please do NOT book your flights yet until we can speak with you!</p>
                          <p style="margin:0;">Any additional travel perks that were purchased will be distributed by your vacation agent.</p>
                        </td>
                      </tr>
                      <tr>
                        <td class="ty-action-body" style="padding:0 0 24px;font-family:'Inter',Arial,Helvetica,sans-serif;font-size:16px;line-height:1.4;color:#222222;">
                          <p style="margin:0;font-weight:700;">Reservation Department Hours</p>
                          <p style="margin:0;font-weight:500;">Monday&ndash;Friday: 10 AM &ndash; 4 PM ET</p>
                        </td>
                      </tr>
                      <tr>
                        <td align="center" style="padding:0;">
                          <table role="presentation" class="ty-cta-wrap" cellpadding="0" cellspacing="0" border="0" align="center" width="100%" style="border-radius:40px;background-color:#e5701c;max-width:100%;">
                            <tr>
                              <td align="center" style="padding:20px 36px;border-radius:40px;">
                                <a href="tel:%PHONE%" style="display:inline-block;font-family:'Roboto',Arial,Helvetica,sans-serif;font-size:16px;font-weight:500;line-height:1;color:#ffffff;text-decoration:none;text-transform:uppercase;">Call Now %PHONE%</a>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Vacation summary -->
          <tr>
            <td class="ty-pad-summary" style="padding:32px 24px 24px;border-top:1px solid #e5e5e5;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 32px;">
                <tr>
                  <td class="ty-icon-cell" style="padding:0 8px 0 0;line-height:0;vertical-align:middle;">{icon_luggage(24)}</td>
                  <td class="ty-summary-h" style="vertical-align:middle;font-family:'Inter',Arial,Helvetica,sans-serif;font-size:24px;font-weight:700;line-height:1.2;color:#071330;">Your Vacation Summary</td>
                </tr>
              </table>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#dfdfdf" style="border-radius:16px;">
                <tr>
                  <td style="padding:1px;border-radius:16px;">
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f9f9f9" style="border-radius:15px;">
                      <tr>
                        <td class="ty-summary-card" style="padding:32px 24px;">
                          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                            <tr>
                              <td style="padding:0 0 24px;">
                                <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                                  <tr>
                                    <td class="ty-icon-cell" width="32" valign="middle" style="width:32px;padding:0 8px 0 0;line-height:0;">{icon_luggage(24)}</td>
                                    <td class="ty-vp-title" valign="middle" style="font-family:'Inter',Arial,Helvetica,sans-serif;font-size:18px;font-weight:700;color:#205272;">Vacation package</td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
{summary_inner}
                          </table>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Legal / terms -->
          <tr>
            <td class="ty-pad-legal" style="padding:40px 24px;background-color:#f4f4f5;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{LEGAL}
              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td class="ty-pad-footer" align="center" style="padding:48px 32px;background-color:#ffffff;border-top:1px solid #f7f7f7;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="center" style="padding:0 0 40px;line-height:0;">
                    <img src="../public/footer-assets/logo.png" width="160" height="47" alt="Exploria Resorts" style="width:160px;max-width:100%;height:auto;margin:0 auto;display:block;" />
                  </td>
                </tr>
                <tr>
                  <td class="ty-footer-copy" align="center" style="padding:0 0 40px;font-family:'Montserrat',Arial,Helvetica,sans-serif;font-size:14px;line-height:1.5;color:#666666;">
                    The vacation package being offered is provided by Club Exploria, LLC, the developer and seller of Club Exploria, a multi-site timeshare plan. &copy; 2026 Club Exploria, LLC. All rights reserved.
                  </td>
                </tr>
                <tr>
                  <td class="ty-footer-discl" align="center" style="padding:0 0 24px;font-family:'Montserrat',Arial,Helvetica,sans-serif;font-size:14px;line-height:1.5;font-weight:700;color:#666666;">
                    THIS ADVERTISING MATERIAL IS BEING USED FOR THE PURPOSE OF SOLICITING SALES OF A VACATION OWNERSHIP PLAN.
                  </td>
                </tr>
                <tr>
                  <td class="ty-footer-discl" align="center" style="padding:0 0 24px;font-family:'Montserrat',Arial,Helvetica,sans-serif;font-size:14px;line-height:1.5;font-weight:700;color:#666666;">
                    THE COMPLETE OFFERING TERMS ARE CONTAINED IN A PUBLIC OFFERING PLAN AVAILABLE FROM THE SPONSOR.
                  </td>
                </tr>
                <tr>
                  <td align="center" style="font-family:'Montserrat',Arial,Helvetica,sans-serif;font-size:14px;line-height:1.5;font-weight:700;">
                    <a href="#" style="color:#000dff;text-decoration:none;">Terms &amp; Conditions</a>
                    <span style="color:#696566;font-weight:600;"> | </span>
                    <a href="#" style="color:#000dff;text-decoration:none;">Privacy Policy</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


VARIANTS = [
    (
        "thank-you-orlando.html",
        "Exploria Thank You — Orlando",
        "../public/ty-emails/orlando-hero.png",
        "Complimentary Owners Getaway at Summer Bay Orlando by Exploria Resorts",
        "Your Orlando getaway includes your choice of a $100 Resort Credit or a $100 Ticket Credit at Summer Bay Orlando by Exploria Resorts.",
    ),
    (
        "thank-you-daytona.html",
        "Exploria Thank You — Daytona Beach",
        "../public/ty-emails/Daytona%20header%201.png",
        "Complimentary Owners Getaway at Grand Seas by Exploria Resorts, Daytona Beach",
        "Your Daytona Beach getaway includes your choice of a $100 Resort Credit or a $100 Ticket Credit at Grand Seas by Exploria Resorts.",
    ),
    (
        "thank-you-poconos.html",
        "Exploria Thank You — Poconos",
        "../public/ty-emails/poconos%20header%201.png",
        "Complimentary Owners Getaway at Poconos Mountain Villas by Exploria Resorts",
        "Your Poconos getaway includes your choice of four (4) Indoor Waterpark Passes or four (4) Zipline Tickets at Poconos Mountain Villas by Exploria Resorts.",
    ),
]


def main() -> None:
    for filename, title, hero, includes, bonus in VARIANTS:
        html = build_html(title, hero, includes, bonus)
        (ROOT / filename).write_text(html, encoding="utf-8")
        print("Wrote", filename)


if __name__ == "__main__":
    main()
