// Generated from c:/Users/User/OneDrive/Documenten/Open Universiteit/IB9902 Voorbereiden Afstuderen/sycococopy/antlrFiles/Pythonic.g4 by ANTLR 4.13.1

from antlr_denter.DenterHelper import DenterHelper
from PythonicParser import PythonicParser

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class PythonicLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROTOCOL=1, ROLES=2, TO=3, FROM=4, SEND=5, SEQUENCE=6, SHUFFLE=7, CHOICE=8, 
		REPEAT=9, LOOP=10, CLOSE=11, LOOPLABEL=12, WORD=13, WS=14, NL=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", "CHOICE", 
			"REPEAT", "LOOP", "CLOSE", "LOOPLABEL", "WORD", "WS", "NL"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
			"'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
			"CHOICE", "REPEAT", "LOOP", "CLOSE", "LOOPLABEL", "WORD", "WS", "NL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	class MyCoolDenter(DenterHelper):
	    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
	        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
	        self.lexer: PythonicLexer = lexer

	    def pull_token(self):
	        return super(PythonicLexer, self.lexer).nextToken()

	denter = None

	def nextToken(self):
	    if not self.denter:
	        self.denter = self.MyCoolDenter(self, self.NL, PythonicParser.INDENT, PythonicParser.DEDENT, False)
	    return self.denter.next_token()



	public PythonicLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Pythonic.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000f\u0080\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0004\fo\b\f\u000b\f\f\fp\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0003\u000ex\b\u000e\u0001\u000e\u0001\u000e\u0005\u000e|\b\u000e"+
		"\n\u000e\f\u000e\u007f\t\u000e\u0000\u0000\u000f\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u0001\u0000\u0001"+
		"\u0004\u000009AZ__az\u0082\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0001\u001f\u0001\u0000"+
		"\u0000\u0000\u0003)\u0001\u0000\u0000\u0000\u00050\u0001\u0000\u0000\u0000"+
		"\u00073\u0001\u0000\u0000\u0000\t8\u0001\u0000\u0000\u0000\u000b=\u0001"+
		"\u0000\u0000\u0000\rG\u0001\u0000\u0000\u0000\u000fP\u0001\u0000\u0000"+
		"\u0000\u0011X\u0001\u0000\u0000\u0000\u0013_\u0001\u0000\u0000\u0000\u0015"+
		"d\u0001\u0000\u0000\u0000\u0017j\u0001\u0000\u0000\u0000\u0019n\u0001"+
		"\u0000\u0000\u0000\u001br\u0001\u0000\u0000\u0000\u001dw\u0001\u0000\u0000"+
		"\u0000\u001f \u0005p\u0000\u0000 !\u0005r\u0000\u0000!\"\u0005o\u0000"+
		"\u0000\"#\u0005t\u0000\u0000#$\u0005o\u0000\u0000$%\u0005c\u0000\u0000"+
		"%&\u0005o\u0000\u0000&\'\u0005l\u0000\u0000\'(\u0005:\u0000\u0000(\u0002"+
		"\u0001\u0000\u0000\u0000)*\u0005r\u0000\u0000*+\u0005o\u0000\u0000+,\u0005"+
		"l\u0000\u0000,-\u0005e\u0000\u0000-.\u0005s\u0000\u0000./\u0005:\u0000"+
		"\u0000/\u0004\u0001\u0000\u0000\u000001\u0005t\u0000\u000012\u0005o\u0000"+
		"\u00002\u0006\u0001\u0000\u0000\u000034\u0005f\u0000\u000045\u0005r\u0000"+
		"\u000056\u0005o\u0000\u000067\u0005m\u0000\u00007\b\u0001\u0000\u0000"+
		"\u000089\u0005s\u0000\u00009:\u0005e\u0000\u0000:;\u0005n\u0000\u0000"+
		";<\u0005d\u0000\u0000<\n\u0001\u0000\u0000\u0000=>\u0005s\u0000\u0000"+
		">?\u0005e\u0000\u0000?@\u0005q\u0000\u0000@A\u0005u\u0000\u0000AB\u0005"+
		"e\u0000\u0000BC\u0005n\u0000\u0000CD\u0005c\u0000\u0000DE\u0005e\u0000"+
		"\u0000EF\u0005:\u0000\u0000F\f\u0001\u0000\u0000\u0000GH\u0005s\u0000"+
		"\u0000HI\u0005h\u0000\u0000IJ\u0005u\u0000\u0000JK\u0005f\u0000\u0000"+
		"KL\u0005f\u0000\u0000LM\u0005l\u0000\u0000MN\u0005e\u0000\u0000NO\u0005"+
		":\u0000\u0000O\u000e\u0001\u0000\u0000\u0000PQ\u0005c\u0000\u0000QR\u0005"+
		"h\u0000\u0000RS\u0005o\u0000\u0000ST\u0005i\u0000\u0000TU\u0005c\u0000"+
		"\u0000UV\u0005e\u0000\u0000VW\u0005:\u0000\u0000W\u0010\u0001\u0000\u0000"+
		"\u0000XY\u0005r\u0000\u0000YZ\u0005e\u0000\u0000Z[\u0005p\u0000\u0000"+
		"[\\\u0005e\u0000\u0000\\]\u0005a\u0000\u0000]^\u0005t\u0000\u0000^\u0012"+
		"\u0001\u0000\u0000\u0000_`\u0005l\u0000\u0000`a\u0005o\u0000\u0000ab\u0005"+
		"o\u0000\u0000bc\u0005p\u0000\u0000c\u0014\u0001\u0000\u0000\u0000de\u0005"+
		"c\u0000\u0000ef\u0005l\u0000\u0000fg\u0005o\u0000\u0000gh\u0005s\u0000"+
		"\u0000hi\u0005e\u0000\u0000i\u0016\u0001\u0000\u0000\u0000jk\u0003\u0019"+
		"\f\u0000kl\u0005:\u0000\u0000l\u0018\u0001\u0000\u0000\u0000mo\u0007\u0000"+
		"\u0000\u0000nm\u0001\u0000\u0000\u0000op\u0001\u0000\u0000\u0000pn\u0001"+
		"\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000q\u001a\u0001\u0000\u0000"+
		"\u0000rs\u0005 \u0000\u0000st\u0001\u0000\u0000\u0000tu\u0006\r\u0000"+
		"\u0000u\u001c\u0001\u0000\u0000\u0000vx\u0005\r\u0000\u0000wv\u0001\u0000"+
		"\u0000\u0000wx\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000y}\u0005"+
		"\n\u0000\u0000z|\u0005 \u0000\u0000{z\u0001\u0000\u0000\u0000|\u007f\u0001"+
		"\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000"+
		"~\u001e\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u0005\u0000"+
		"npw}\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}