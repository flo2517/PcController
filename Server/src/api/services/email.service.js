const transporter = require('../../config/mailer.config');

const sendVerifyMail = (email, verifyString) => {
    let sender = 'no-reply'
    let mailOptions = {
        from: sender,
        to: email,
        subject: 'Verify your email',
        text: 'Verify your email',
        html: `<p>Please verify your email by clicking the link below:</p>
        <a href="http://thrall:8080/verify/${verifyString}">Verify</a>`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });
}

module.exports = {
    sendVerifyMail
}