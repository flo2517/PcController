const transporter = require('../../config/mailer.config');
const ejs = require('ejs');

class EmailService {
    
}

EmailService.sendVerifyMail = (email, verifyString) => {

    let sender = process.env.MAIL_USER;
    ejs.renderFile(__dirname + '/../../views/emails/welcomeEmail.ejs', {
        user_firstname: 'You',
        confirm_link: `http://${process.env.API_HOST}:${process.env.API_PORT}/verify/${verifyString}"`
    }).then(function(data) {
        let mailOptions = {
            from: sender,
            to: email,
            subject: 'Welcome to the app',
            html: data
        };
        transporter.sendMail(mailOptions, function(error, info) {
            if (error) {
                console.log(error);
            } else {
                console.log('Email sent: ' + info.response);
            }
        });
    });
}

EmailService.sendResetPasswordMail = (email, passwordToken) => {
    let sender = process.env.MAIL_USER;
    let mailOptions = {
        from: sender,
        to: email,
        subject: 'Reset your password',
        text: 'Reset your password',
        html: `<p>Please reset your password by clicking the link below:</p>
        <a href="http://${process.env.API_HOST}:${process.env.API_PORT}/resetPassword?token=${passwordToken}">Reset</a>`
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
