<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Metro Ticketing System - Python Project</title>
</head>
<body>

    <h1><u>Metro Ticketing System – Python Project</u></h1>

    <h2><u>1. Background</u></h2>
    <p>
        In many cities, buying metro tickets is still a manual process. This causes long queues, wasted time, and mistakes.
        To solve this, I created a simple Python-based Metro Ticketing System that helps users:
    </p>
    <ul>
        <li>Buy single or multiple metro tickets easily</li>
        <li>Cancel tickets with partial refunds</li>
        <li>Generate QR codes for ticket verification</li>
    </ul>

    <h2><u>2. Data Structure</u></h2>
    <p>
        The project is written in Python and uses the following libraries:
    </p>
    <ul>
        <li><strong>pandas</strong> – to handle and store ticket data in CSV format</li>
        <li><strong>qrcode</strong> – to generate QR codes</li>
        <li><strong>os</strong> and <strong>datetime</strong> – to manage file paths and generate unique ticket IDs</li>
    </ul>

    <p>The program flow includes:</p>
    <ul>
        <li>Taking user input for name, phone number, and stations</li>
        <li>Calculating the cost based on station distance</li>
        <li>Generating a ticket ID and QR code</li>
        <li>Saving ticket info into a CSV file</li>
        <li>Allowing ticket cancellation with an 80% refund</li>
    </ul>

    <p><strong>functions:</strong></p>
    <ul>
        <li><img src="E:\programming\github\metro_project\single_ticket.png" alt="Ticket Generation Screenshot" width="500"></li>
        <li><img src="E:\programming\github\metro_project\qr_code.png" alt="QR Code Display" width="300"></li>
    </ul>

    <h2><u>3. Summary</u></h2>
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>Terminal-based interface for ticket purchasing</li>
        <li>Single and multiple ticket options</li>
        <li>QR code generation</li>
        <li>Ticket cancellation with refund</li>
        <li>Data saved in a CSV file</li>
    </ul>

    <p><strong>Real-World Benefits:</strong></p>
    <ul>
        <li>Helps avoid manual errors and save time</li>
        <li>Simple prototype for real metro station ticketing</li>
        <li>Promotes digital solutions for local transport</li>
    </ul>

    <h2><u>4. Recommendation</u></h2>
    <p>
        If you have any suggestions, feedback, or want to collaborate, feel free to open an issue or pull request on GitHub.
        Your ideas and contributions are always welcome.
    </p>
    <p>
        <strong>Have any questions or thoughts?</strong> Please reach out — I’d love to hear from you.
    </p>

    <p><em>Created by Saqib Hassan</em></p>

</body>
</html>
