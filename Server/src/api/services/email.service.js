const transporter = require('../../config/mailer.config');

class EmailService {
    
}

EmailService.sendVerifyMail = (email, verifyString) => {
    let sender = 'admin@thrallweb.fr'
    let mailOptions = {
        from: sender,
        to: email,
        subject: 'Verify your email',
        text: 'Verify your email',
        html: `<p>Please verify your email by clicking the link below:</p>
        <a href="http://thrallweb.fr:8080/verify/${verifyString}">Verify</a>`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' , info);
        }
    });
}

module.exports = EmailService;
