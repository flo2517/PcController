const transporter = require('../../config/mailer.config');

class EmailService {
    
}

EmailService.sendVerifyMail = (email, verifyString) => {
    let sender = process.env.MAIL_USER;
    let mailOptions = {
        from: sender,
        to: email,
        subject: 'Verify your email',
        text: 'Verify your email',
        html: `<p>Please verify your email by clicking the link below:</p>
        <a href="http://${process.env.API_HOST}:${process.env.API_PORT}/verify/${verifyString}">Verify</a>`
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
